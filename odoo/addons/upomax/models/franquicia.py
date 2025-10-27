from odoo import models, fields, api

class franquicia(models.Model):
    _name = 'upomax.franquicia'
    _description = 'Franquicia'

    nombre = fields.Char(string="Nombre de la Franquicia", required=True, size=100)
    _sql_constraints = [
        ('nombre_unique', 'UNIQUE(nombre)', 'El nombre de la franquicia debe ser único.')
    ]
    descripcion = fields.Char(string="Descripción", size=100)
    anio_inicio = fields.Date(string="Año de Inicio")
    estado = fields.Char(string="Estado", size=50)
    titulo = fields.Char(string="Título Asociado", size=100)