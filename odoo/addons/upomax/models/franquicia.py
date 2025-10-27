from odoo import models, fields, api

class franquicia(models.Model):
    _name = 'upomax.franquicia'
    _description = 'Franquicia'

    nombre = fields.Char(string="Nombre de la Franquicia", required=True)
    _sql_constraints = [
        ('nombre_unique', 'UNIQUE(nombre)', 'El nombre de la franquicia debe ser único.')
    ]
    descripcion = fields.Char(string="Descripción")
    anio_inicio = fields.Date(string="Año de Inicio")
    estado = fields.Char(string="Estado")
    titulo = fields.Char(string="Título Asociado")