from odoo import models, fields, api

class plataforma(models.Model):
    _name = 'upomax.plataforma'
    _description = 'Plataforma'

    name = fields.Char(string="Nombre de la Plataforma", required=True, size=100)
    

    series_ids= fields.Many2many("upomax.serie",string="Series confirmadas") 