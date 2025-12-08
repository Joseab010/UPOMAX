from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Pelicula(models.Model):
    _name = 'upomax.pelicula'
    _description = 'Película'

    name = fields.Char(string="Título", required=True, size=100)
    descripcion = fields.Text(string="Descripción", size=500)
    puntuacion_general = fields.Float(string="Puntuación General", digits=(2, 2), compute='_compute_puntuacion_general', store=True)
    anio = fields.Date(string="Año de Estreno")
    edad_recomendada = fields.Integer(string="Edad Recomendada")
    duracion = fields.Integer(string="Duración (minutos)")
    
    plataformas_ids = fields.Many2many(
        "upomax.plataforma",
        'rel_plataforma_pelicula',
        'pelicula_id',
        'plataforma_id',
        string="Plataformas confirmadas"
    )
    
    nombre_franquicia_id = fields.Many2one('upomax.franquicia', inverse_name="peliculas_ids", string='Franquicia')
    nombre_banda_id = fields.Many2one('upomax.banda.sonora', inverse_name='peliculas_ids', string='Banda Sonora') 
    
    generos_ids = fields.Many2many(
        'upomax.genero',           
        'rel_genero_pelicula',        
        'pelicula_id',               
        'genero_id',               
        string="Géneros"
    )

    productoras_ids = fields.Many2many(
        'upomax.productora',           
        'rel_productora_pelicula',        
        'pelicula_id',               
        'productora_id',               
        string="Productoras"
    )

    premios_ids = fields.One2many('upomax.premio', inverse_name='titulo_pelicula', string='Premios')
    reviews_ids = fields.One2many('upomax.review', inverse_name='pelicula_id', string='Reseñas')
    participacion_ids = fields.One2many('upomax.persona.tipo', 'pelicula_id', string="Participaciones")
    
    # Campos One2many filtrados
    directores_ids = fields.One2many(
        'upomax.persona.tipo', 
        'pelicula_id', 
        domain=[('tipo_id.name', '=', 'Director')],
        string="Directores"
    )
    actores_ids = fields.One2many(
        'upomax.persona.tipo', 
        'pelicula_id', 
        domain=[('tipo_id.name', '=', 'Actor')],
        string="Actores"
    )
    compositores_ids = fields.One2many(
        'upomax.persona.tipo', 
        'pelicula_id', 
        domain=[('tipo_id.name', '=', 'Compositor')],
        string="Compositores"
    )
    
    @api.constrains('duracion')
    def _check_duracion(self):  
        for rec in self:
            if rec.duracion <= 0:
                raise ValidationError("La duración debe ser positiva.")
   
    @api.constrains('descripcion')     
    def _check_descripcion(self):         
        for rec in self:             
            if rec.descripcion and len(rec.descripcion) > 500:      
                raise ValidationError(f"La descripción es demasiado larga. Tienes {len(rec.descripcion)} caracteres, límite 500.")
            
    @api.depends('reviews_ids.calificacion')   
    def _compute_puntuacion_general(self):
        for pelicula in self:
            if pelicula.reviews_ids:
                calificaciones = [r.calificacion for r in pelicula.reviews_ids]
                promedio = sum(calificaciones) / len(calificaciones)
                pelicula.puntuacion_general = promedio
            else:
                pelicula.puntuacion_general = 0.0        

    @api.constrains('edad_recomendada')
    def _check_edad_recomendada(self):
        for rec in self:
            if rec.edad_recomendada < 0:
                raise ValidationError("La edad recomendada no puede ser negativa.")
            if rec.edad_recomendada > 18:
                raise ValidationError("La edad recomendada suele ser hasta 18 años.")
            
    @api.constrains('name', 'anio')
    def _check_pelicula_unica(self):
        for rec in self:
            if rec.name and rec.anio:
                domain = [
                    ('name', '=ilike', rec.name), 
                    ('anio', '=', rec.anio),      
                    ('id', '!=', rec.id)          
                ]
                if self.search_count(domain) > 0:
                    raise ValidationError(f"Ya existe una película llamada '{rec.name}' estrenada en {rec.anio}.")