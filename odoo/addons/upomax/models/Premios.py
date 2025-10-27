from odoo import models, fields, api


class Premios(models.Model):
    _name = 'upomax.premios'
    _description = 'Tabla con informacion de las premios'

    nombre = fields.char(
            'upomax.nombrepremio', 
            string="Nombre del Premio",
            required=True,size=100,
            help="Ej: Oscars, Emmys, Globos de Oro")
    
    categoria= fields.char(
        'upomax.categorias', 
        string="Categoría",
        required=True,size=100,
        help="Ej: Mejor Serie Dramática, Mejor Actor")

    año=fields.Date(string="Año de emision",requiered=True)

    titulo=fields.char('upomax.serie', 
        string="Serie",
        required=True,
        help="La serie que recibió el premio.")