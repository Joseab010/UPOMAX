from odoo import models, fields, api


class Banda_sonora(models.Model):
    _name = 'upomax.banda.sonora'
    _description = 'Tabla con informacion de las bandas sonoras'
    
    name = fields.Char(string="Nombre_BSO", required=True,size=100, help="Nombre de BSO")
    
   
    anyo = fields.Date(string="fecha de salida")
    pais = fields.Char(string="Pais", size=100)
    peliculas_ids= fields.One2many("upomax.pelicula","nombre_banda_id",string="Peliculas confirmadas")
