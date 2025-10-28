from odoo import models, fields, api


class Banda_sonora(models.Model):
    _name = 'upomax.Banda_sonora'
    _description = 'Tabla con informacion de las bandas sonoras'
    
    Nombre_BSO = fields.Char(string="Nombre_BSO", required=True,size=100, help="Nombre de BSO")
    #titulo fK
    Titulo = fields.Char(string="correo_electronico", size=100,required=True, help="Nombre de Titulo")
    Año = fields.Date(string="fecha de salida")
    Pais = fields.Char(string="Pais", size=100)
