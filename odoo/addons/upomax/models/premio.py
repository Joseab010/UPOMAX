from odoo import models, fields, api


class premio(models.Model):
    
    _name = 'upomax.premio'
    _description = 'Tabla con informacion de las premio'

    name = fields.char(
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

    titulo_serie=fields.One2one('upomax.serie', 
        string="Serie",
        required=True,
        help="La serie que recibió el premio.")
    
    titulo_pelicula=fields.One2one('upomax.pelicula', 
        string="Pelicula",
        required=True,
        help="La serie que recibió el premio.")