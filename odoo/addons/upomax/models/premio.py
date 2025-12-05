from odoo import models, fields, api

class Premio(models.Model):
    _name = 'upomax.premio'
    _description = 'Tabla con informacion de los premios'

    name = fields.Char(
            string="Nombre del Premio",
            required=True, size=100,
            help="Ej: Oscars, Emmys, Globos de Oro")
    
    categoria = fields.Char(
        string="Categoría",
        required=True, size=100,
        help="Ej: Mejor Serie Dramática, Mejor Actor")

    ano = fields.Date(string="Año de emision", required=True)

   
    titulo_serie = fields.Many2one('upomax.serie', 
        string="Serie",
        help="La serie que recibió el premio.")
    
    titulo_pelicula = fields.Many2one('upomax.pelicula', 
        string="Pelicula",
        help="La película que recibió el premio.")
    
    
    series_count = fields.Integer(
        string="Nº Series", 
        compute='_compute_conteo', 
        store=True
    )
   
    peliculas_count = fields.Integer(
        string="Nº Películas", 
        compute='_compute_conteo', 
        store=True
    )

    @api.depends("titulo_serie","titulo_pelicula")
    def _compute_conteo(self):
        for record in self:
            record.peliculas_count = 1 if record.titulo_pelicula else 0
            record.series_count = 1 if record.titulo_serie else 0