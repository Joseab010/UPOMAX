from odoo import models, fields, api


class Serie(models.Model):
    _name = 'upomax.serie'
    _description = 'Tabla con informacion de las series'

    name = fields.Char(string="Titulo", required=True,size=100)
    fecha_emision=fields.Date(string="fecha de emision")
    fecha_finalizacion=fields.Date(string="fecha de finalizacion")
    duracion = fields.Integer(string="Duración (min)")
    
    plataformas_ids = fields.Many2many(
        'upomax.plataforma',
        'rel_plataforma_serie',
        'serie_id',
        'plataforma_id',
        string="Plataformas confirmadas"
    )
    
    