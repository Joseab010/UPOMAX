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

    serie_id = fields.Many2one('upomax.serie', string='Serie')
    capitulo_ids = fields.One2many('upomax.capitulo',
                                   'temporada_id',
                                   string='Capítulos de la Temporada')
    
    