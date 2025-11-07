from odoo import models, fields, api

class plataforma(models.Model):
    _name = 'upomax.plataforma'
    _description = 'Plataforma'

    name = fields.Char(string="Nombre de la Plataforma", required=True, size=100)


    series_ids = fields.Many2many(
        'upomax.serie',
        'rel_plataforma_serie',
        'plataforma_id',
        'serie_id',
        string="Series confirmadas"
    ) 
    peliculas_ids = fields.Many2many(
        'upomax.peliculas',
        'rel_plataforma_pelicula',
        'plataforma_id',
        'pelicula_id',
        string="Peliculas confirmadas"
    ) 