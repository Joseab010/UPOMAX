from odoo import models, fields, api


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


    persona_ids = fields.Many2many('upomax.tipo', 
                                    'rel_capitulo_persona', 
                                    'capitulo_id',
                                    'persona_tipo_id',
                                    string="Persona con participación específica",
                                    required=True)

    #uso de capa ORM ma g 

    

    
