from odoo import models, fields, api


class Serie(models.Model):
    _name = 'upomax.serie'
    _description = 'Tabla con informacion de las series'

    titulo = fields.Char(string="Titulo", required=True,size=100, help="Titulo principal de la serie")
    fecha_emision=fields.Date(string="fecha de emision")
    fecha_finalizacion=fields.Date(string="fecha de finalizacion")

    duracion = fields.Integer(
        string="Duración (min)", 
        help="Duración de una serie en minutos"
    )