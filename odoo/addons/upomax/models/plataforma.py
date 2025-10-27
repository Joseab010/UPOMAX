from odoo import models, fields, api

class plataforma(models.Model):
    _name = 'upomax.plataforma'
    _description = 'Plataforma'

    nombre = fields.Char(string="Nombre de la Plataforma", required=True, size=100)
    _sql_constraints = [
        ('nombre_unique', 'UNIQUE(nombre)', 'El nombre de la plataforma debe ser único.')
    ]