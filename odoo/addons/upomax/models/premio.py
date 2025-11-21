from odoo import models, fields, api


class premio(models.Model):
    
    _name = 'upomax.premio'
    _description = 'Tabla con informacion de las premio'

    name = fields.Char(
            string="Nombre del Premio",
            required=True,size=100,
            help="Ej: Oscars, Emmys, Globos de Oro")
    
    categoria= fields.Char(
        string="Categoría",
        required=True,size=100,
        help="Ej: Mejor Serie Dramática, Mejor Actor")

    año=fields.Date(string="Año de emision",required=True)

    titulo_serie=fields.Many2one('upomax.serie', 
        string="Serie",
        help="La serie que recibió el premio.")
    
    titulo_pelicula=fields.Many2one('upomax.pelicula', 
        string="Pelicula",
        help="La película que recibió el premio.")