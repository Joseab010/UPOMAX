from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Serie(models.Model):
    _name = 'upomax.serie'
    _description = 'Tabla con informacion de las series'

    name = fields.Char(string="Titulo", required=True, size=100)
    fecha_emision = fields.Date(string="Fecha de emision")
    fecha_finalizacion = fields.Date(string="Fecha de finalizacion")
    duracion = fields.Integer(string="Duración (min)")
    edad_recomendada = fields.Integer(string="Edad Recomendada")
    puntuacion_general = fields.Float(
        string="Puntuación General", 
        digits=(2, 2), 
        compute='_compute_puntuacion_general', 
        store=True
    )

    plataformas_ids = fields.Many2many(
        'upomax.plataforma',
        'rel_plataforma_serie',
        'serie_id',
        'plataforma_id',
        string="Plataformas confirmadas"
    )
    
    generos_ids = fields.Many2many(
        'upomax.genero',          
        'rel_genero_serie',       
        'serie_id',               
        'genero_id',              
        string="Géneros"
    )
  
    # Asegúrate de que los modelos relacionados (upomax.temporada, etc.) existan y estén cargados
    temporadas_ids = fields.One2many('upomax.temporada', inverse_name='serie_id', string='Temporada')
    premios_ids = fields.One2many('upomax.premio', inverse_name='titulo_serie', string='Premios')
    reviews_ids = fields.One2many('upomax.review', inverse_name='serie_id', string='Reseñas')
    participacion_ids = fields.One2many('upomax.persona.tipo', 'serie_id', string="Participaciones")
    
    @api.constrains("duracion")
    def _check_duracion(self):
        
        for record in self:
            if record.duracion < 0:
                raise ValidationError("La duración no puede ser negativa")

    @api.depends('reviews_ids.calificacion')   
    def _compute_puntuacion_general(self):
        for serie in self:
            if serie.reviews_ids:
                calificaciones = [r.calificacion for r in serie.reviews_ids]
                promedio = sum(calificaciones) / len(calificaciones)
                serie.puntuacion_general = promedio
            else:
                serie.puntuacion_general = 0.0