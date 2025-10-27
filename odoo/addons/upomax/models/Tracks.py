from odoo import models, fields, api


class Tracks(models.Model):
    _name = 'upomax.Tracks'
    _description = 'Tabla con informacion de los tracks'
    
    titulo_trakc = fields.Char(string="titulo", size=100,required=True)
    Nombre_tipo = fields.Integer(string="Duracion (min)") 