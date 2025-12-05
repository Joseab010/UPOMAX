from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class Capitulo(models.Model):
    _name = 'upomax.capitulo'
    _description = 'Información del Capítulo'

    name = fields.Char(
        string="Título del capítulo", 
        required=True, 
        size=100,
        help="Ej: 'Capítulo 1'"
    )
    
    
    fecha_emision = fields.Date(string="Fecha de Emisión")

    num_capitulo = fields.Integer(
        string="Número de capítulo",
        required=True, 
        help="Ej: 1, 2, 3..."
    )

    duracion = fields.Integer(string="Duración (min)")

    temporada_id = fields.Many2one(
        'upomax.temporada',
        string='Temporada',
        required=True
    )

    participacion_ids = fields.One2many(
        'upomax.persona.tipo', 
        'capitulo_id', 
        string="Participaciones"
    )
    
    tracks_ids = fields.One2many(
        "upomax.track", 
        "capitulo_id", 
        string="Tracks del capítulo"
    )

    serie_id = fields.Many2one(
        'upomax.serie',
        string='Serie',
        required=True
    )
    
    @api.constrains("duracion")
    def _check_duracion(self):
        for record in self:
            if record.duracion < 0:
                raise ValidationError("La duración no puede ser negativa")