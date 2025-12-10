from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re    #para las expresiones regulares

class Usuario(models.Model):
    _name = 'upomax.usuario'
    _description = 'Tabla con informacion de los usuarios'
    
    name = fields.Char(string="Nombre usuario", required=True,size=100, help="Nombre de Usuario")
    correo_Electronico = fields.Char(string="Correo electronico", size=100,required=True, help="Nombre de Correo")
    contrasenya = fields.Char(string="Contraseña", size=100,required=True, help="Contraseña usuario")
    biografia = fields.Char(string="biografia", size=400, help="biografia de usuario")

    recomendaciones_texto = fields.Text(string="Te recomendamos que veas...", readonly=True)


    reviews_ids = fields.One2many('upomax.review',inverse_name='id_usuario',string="Reseñas de usuarios")
    lista_ids = fields.One2many('upomax.lista', 'usuario_id', string="Listas del Usuario")
    
    amigos_ids = fields.Many2many('upomax.usuario',
                                  'rel_usuario_amistad',
                                  'usuario_id',
                                  'amigo_id',
                                  string="Lista de amigos")
    

    def action_generar_recomendaciones(self):
       # 1. Ejecutar la IA
        self.env['upomax.ai.recommender'].train_and_predict(specific_user_id=self.id)
        
        # 2. Notificación visual (Arriba a la derecha)
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Inteligencia Artificial',
                'message': 'El modelo ha sido re-entrenado y las recomendaciones actualizadas.',
                'type': 'success',  # types: success, warning, danger, info
                'sticky': False,
            }
        }
        
        # 3. Recargar la vista para ver los cambios
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',  # Esto fuerza a Odoo a refrescar la ficha del usuario
            'params': {'next': notification} # Encadenamos la notificación
        }


    #Validacion para el nombre
    @api.constrains('name')
    def _check_name(self):
        for rec in self:
            if not rec.name or len(rec.name.strip()) < 3:
                raise ValidationError("El nombre debe tener al menos 3 caracteres.")
            if not re.match(r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]+$', rec.name):
                raise ValidationError("El nombre solo puede contener letras y espacios.")      
    
    #Validacion para el correo
    @api.constrains('correo_Electronico')
    def _check_email(self):
        for rec in self:
            if not rec.correo_Electronico:
                raise ValidationError("El correo no puede estar vacio.")
            if not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', rec.correo_Electronico):
                raise ValidationError("El email no cumple el formato.") 
    
    #Validacion para password    
    @api.constrains('contrasenya')     
    def _check_password(self):         
        for rec in self:             
            if not rec.contrasenya:            
                raise ValidationError("La contraseña no puede estar vacia.")           
            if not re.match(r'^(?=(?:.*\d){4,})(?=.*[a-z])(?=.*[A-Z]).*$', rec.contrasenya):        
                raise ValidationError("La contraseña no cumple el formato debe contener al menos una mayuscula, una minuscula y 4 dígitos.") 

    #Validacion para biografia    
    @api.constrains('biografia')     
    def _check_biografia(self):         
        for rec in self:             
            if rec.biografia and len(rec.biografia)>400:      
                raise ValidationError(f"La biografía es demasiado larga. Tienes {len(rec.biografia)} caracteres, pero el límite es 400.")

    @api.constrains('amigos_ids')
    def _check_amigos(self):
        for rec in self:
            if rec.id in rec.amigos_ids.ids:
                raise ValidationError("No puedes añadirte a ti mismo como amigo.")
            