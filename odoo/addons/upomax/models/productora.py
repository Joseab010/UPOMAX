from odoo import models, fields, api

class productora(models.Model):
    _name = 'upomax.productora'
    _description = 'Productora'

    nombre_productora = fields.Char(string="Nombre de la Productora", required=True, size=100)
    _sql_constraints = [
        ('nombre_productora_unique', 'UNIQUE(nombre_productora)', 'El nombre de la productora debe ser único.')
    ]
    fundacion = fields.Date(string="Fecha de Fundación")
    pais = fields.Char(string="País", size=50)
    titulo = fields.Char(string="Título Asociado", size=100)