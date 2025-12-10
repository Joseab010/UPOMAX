from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)

try:
    import numpy as np
    import scipy.optimize as opt
    HAS_DEPS = True
except ImportError:
    HAS_DEPS = False
    _logger.warning("Numpy or Scipy not installed. UPOMAX AI features disabled.")

class AIRecommender(models.AbstractModel):
    _name = 'upomax.ai.recommender'
    _description = 'Motor de IA para Recomendaciones'

    def _cofi_cost_func_reg(self, params, Y, R, num_features, lambda_param):
        num_items = Y.shape[0]
        num_users = Y.shape[1]
        
        punto_corte = num_items * num_features
        X = params[:punto_corte].reshape(num_items, num_features)
        Theta = params[punto_corte:].reshape(num_features, num_users) 

        prediction = np.dot(X, Theta)
        
        error = (prediction - Y) * R 
        
        J = 0.5 * np.sum(error**2)
        J += (lambda_param / 2.0) * (np.sum(Theta**2) + np.sum(X**2))
        
        return J

    def _cofi_gradient_func_reg(self, params, Y, R, num_features, lambda_param):
   
        num_items = Y.shape[0]
        num_users = Y.shape[1]
        
        punto_corte = num_items * num_features
        X = params[:punto_corte].reshape(num_items, num_features)
        Theta = params[punto_corte:].reshape(num_features, num_users)

        prediction = np.dot(X, Theta)
        error = (prediction - Y) * R

        
        X_grad = np.dot(error, Theta.T) + (lambda_param * X)
        Theta_grad = np.dot(X.T, error) + (lambda_param * Theta)

        return np.concatenate((X_grad.flatten(), Theta_grad.flatten()))


    def train_and_predict(self, specific_user_id=None):
       
        if not HAS_DEPS:
            _logger.warning("Operación cancelada: numpy y scipy son necesarios para esta función.")
            return

    

        # 1. Obtener datos de Odoo
        # Necesitamos todas las reviews, usuarios y contenidos (peliculas y series)
        Review = self.env['upomax.review']
        reviews = Review.search([('calificacion', '>', 0)]) # Solo reviews con nota

        # 2. Mapeo de IDs de Odoo a Índices de Matriz (0, 1, 2...)
        # Esto es vital para mezclar Pelis y Series
        user_map = {}   # {odoo_user_id: matrix_index}
        item_map = {}   # {('p', pelicula_id): matrix_index, ('s', serie_id): matrix_index}
        inverse_item_map = {} # {matrix_index: ('type', odoo_id)}

        u_idx = 0
        i_idx = 0

        # Listas para construir la matriz Y
        data_points = [] # [(user_idx, item_idx, rating)]

        for r in reviews:
            # Mapeo de Usuario
            if r.id_usuario.id not in user_map:
                user_map[r.id_usuario.id] = u_idx
                u_idx += 1
            
            # Mapeo de Item (Detectar si es Peli o Serie)
            key = None
            if r.pelicula_id:
                key = ('pelicula', r.pelicula_id.id)
            elif r.serie_id:
                key = ('serie', r.serie_id.id)
            
            if key:
                if key not in item_map:
                    item_map[key] = i_idx
                    inverse_item_map[i_idx] = key
                    i_idx += 1
                
                # Guardamos el dato temporalmente
                data_points.append((user_map[r.id_usuario.id], item_map[key], r.calificacion))

        num_users = u_idx
        num_items = i_idx
        
        if num_users == 0 or num_items == 0:
            _logger.warning("No hay suficientes datos para entrenar el modelo.")
            if specific_user_id:
                self.env['upomax.usuario'].browse(specific_user_id).write({
                    'recomendaciones_texto': "¡Vaya! Aún no tenemos suficientes datos globales para recomendarte nada.\nIntenta hacer algunas reviews primero."
                })
            return

        # 3. Construir Matrices Y (Ratings) y R (Vistos)
        Y = np.zeros((num_items, num_users))
        R = np.zeros((num_items, num_users))

        for u, i, rating in data_points:
            Y[i, u] = rating
            R[i, u] = 1

        # 4. Inicialización Aleatoria 
        num_features = 10 # Latent factors
        X = np.random.randn(num_items, num_features)
        Theta = np.random.randn(num_features, num_users)
        
        initial_params = np.concatenate((X.flatten(), Theta.flatten()))
        lambda_reg = 1.5

        # 5. Optimización 
        result_params = opt.fmin_cg(
            f=self._cofi_cost_func_reg,
            x0=initial_params,
            fprime=self._cofi_gradient_func_reg,
            args=(Y, R, num_features, lambda_reg),
            maxiter=100, # Reducido para que no bloquee Odoo demasiado tiempo
            disp=False
        )

        # 6. Reconstruir matrices entrenadas
        punto_corte = num_items * num_features
        X_trained = result_params[:punto_corte].reshape(num_items, num_features)
        Theta_trained = result_params[punto_corte:].reshape(num_features, num_users)

        # 7. Predecir y Guardar resultados
        # P = X * Theta
        Predictions = np.dot(X_trained, Theta_trained)

        # Guardar recomendaciones en el modelo de Usuario
        # Recorremos cada usuario de Odoo mapeado
        for odoo_user_id, matrix_u_idx in user_map.items():
            user_predictions = Predictions[:, matrix_u_idx]
            
            # Obtener índices de ítems que NO ha visto (R[i, u] == 0)
            # Queremos recomendar cosas nuevas
            unseen_indices = np.where(R[:, matrix_u_idx] == 0)[0]
            
            # Crear lista de tuplas (score, matrix_item_idx) solo de lo no visto
            scores = []
            for item_idx in unseen_indices:
                scores.append((user_predictions[item_idx], item_idx))
            
            # Ordenar de mayor a menor score
            scores.sort(key=lambda x: x[0], reverse=True)
            
            # Top 5 recomendaciones
            top_5 = scores[:5]
            
            # Convertir de vuelta a IDs de Odoo y guardar
            recomendaciones_txt = "Te recomendamos:\n"
            ids_peliculas = []
            ids_series = []

            for score, item_idx in top_5:
                type_obj, obj_id = inverse_item_map[item_idx]
                nombre = ""
                if type_obj == 'pelicula':
                    nombre = self.env['upomax.pelicula'].browse(obj_id).name
                    ids_peliculas.append(obj_id) # Para guardar en Many2many si quieres
                    recomendaciones_txt += f"🎬 Película: {nombre} (Predicción: {score:.1f}/10)\n"
                elif type_obj == 'serie':
                    nombre = self.env['upomax.serie'].browse(obj_id).name
                    ids_series.append(obj_id)
                    recomendaciones_txt += f"📺 Serie: {nombre} (Predicción: {score:.1f}/10)\n"

            # Escribir en el usuario
            user_record = self.env['upomax.usuario'].browse(odoo_user_id)
            user_record.write({'recomendaciones_texto': recomendaciones_txt})
            
            _logger.info(f"Recomendaciones publicadas para {user_record.name}")
            
        # 8. Handling Cold Start (Usuario específico sin reviews)
        if specific_user_id and specific_user_id not in user_map:
             self.env['upomax.usuario'].browse(specific_user_id).write({
                 'recomendaciones_texto': "¡Parece que eres nuevo!\nNecesitamos conocer tus gustos. Por favor, escribe algunas reseñas (Reviews) de películas o series para que la IA pueda recomendarte contenido afín a ti."
             })