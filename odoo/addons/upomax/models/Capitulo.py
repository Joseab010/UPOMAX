from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class Capitulos(models.Model):
    _name = 'upomax.capitulo'
    _description = 'Tabla con informacion de las capitulos'

    name = fields.Char(
        string="Título del capitulo", 
        required=True, 
        size=100,
        help="Ej: 'Capitulo 1' "
    )
    
   
    num_capitulo = fields.Integer(
        string="Número de capitulo",
        required=True, 
        help="Ej: 1, 2, 3..."
    )
    

    duracion = fields.Integer(string="Duracion")

    temporada_id = fields.Many2one('upomax.temporada',
                                   string='Temporada',
                                   required=True)

    participacion_ids = fields.One2many('upomax.persona.tipo', 'capitulo_id', string="Participaciones (persona + rol)")


    tracks_ids=fields.One2many("upomax.track","capitulo_id",string="Tracks del capitulo")
    #uso de capa ORM ma g 
    
    @api.constrains("duracion")
    def _check_duracion(self):
        if self.duracion<0:
            raise ValidationError("La duración no puede ser Negativo")
    

    
