from odoo import models, fields, api

class franquicia(models.Model):
    _name = 'upomax.franquicia'
    _description = 'Franquicia'

    name = fields.Char(string="Nombre de la Franquicia", required=True, size=100)
    descripcion = fields.Char(string="Descripción", size=500)
    anio_inicio = fields.Date(string="Año de Inicio")
    estado = fields.Char(string="Estado", size=50)
    
    peliculas_ids= fields.One2many("upomax.peliculas","nombre_franquicia_id",string="Peliculas confirmadas")