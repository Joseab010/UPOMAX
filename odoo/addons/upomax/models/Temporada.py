from odoo import models, fields, api


class temporada(models.Model):
    _name = 'upomax.temporada'
    _description = 'Tabla con informacion de las premios'


    name = fields.Char(
        string="Título de la Temporada", 
        required=True, 
        size=100,
        help="Ej: 'Temporada 1' "
    )
    
   
    num_temporada = fields.Integer(
        string="Número de Temporada",
        required=True, 
        help="Ej: 1, 2, 3..."
    )
    

    cantidad_capitulos = fields.Integer(string="Cantidad de Capítulos")
    serie_id = fields.Many2one('upomax.serie', string='Serie')
    