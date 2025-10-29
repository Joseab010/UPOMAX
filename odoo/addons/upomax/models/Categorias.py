from odoo import models, fields, api


class Categorias(models.Model):
    _name = 'upomax.categorias'
    _description = 'Tabla con informacion de las Categorias'

    categoria=fields.char(String="Categoria",size=100,required=True)