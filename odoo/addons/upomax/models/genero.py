from odoo import models, fields, api

class genero(models.Model):
    _name = 'upomax.genero'
    _description = 'Género'

    tipo_genero = fields.Char(string="Tipo de Género", required=True, size=100)
    _sql_constraints = [
        ('tipo_genero_unique', 'UNIQUE(tipo_genero)', 'El tipo de género debe ser único.')
    ]