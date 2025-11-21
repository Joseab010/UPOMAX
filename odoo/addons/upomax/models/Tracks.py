from odoo import models, fields, api


class Tracks(models.Model):
    _name = 'upomax.track'
    _description = 'Tabla con informacion de los tracks'
    
    name = fields.Char(string="Titulo", size=100,required=True)
    duracion = fields.Integer(string="Duracion (min)") 
    capitulo_id = fields.Many2one('upomax.capitulo',inverse_name= "tracks_ids" ,string='Capitulo')

    
    banda_sonora_id = fields.Many2many('upomax.banda_sonora',
                          'rel_banda_sonora_tracks',
                          'tracks_id',
                          'banda_sonora_id',
                          string='Banda sonora inlcuidas')