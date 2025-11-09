from odoo import models, fields, api


class Tracks(models.Model):
    _name = 'upomax.track'
    _description = 'Tabla con informacion de los tracks'
    
    name = fields.Char(string="titulo", size=100,required=True)
    duracion = fields.Integer(string="Duracion (min)") 
    capitulo_id = fields.Many2one('upomax.capitulo', string='Capitulo')