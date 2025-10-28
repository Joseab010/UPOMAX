from odoo import models, fields, api


class Nombre_premio(models.Model):
    _name = 'upomax.Nombre_premio'
    _description = 'Tabla con informacion de los nombres premios'
    
    nombre_premio = fields.Char(string="Nombre de premio", size=100,required=True)
