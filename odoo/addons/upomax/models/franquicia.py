from odoo import models, fields, api

class franquicia(models.Model):
    _name = 'upomax.franquicia'
    _description = 'Franquicia'

    name = fields.Char(string="Nombre de la Franquicia", required=True, size=100)
    descripcion = fields.Char(string="Descripción", size=500)
    anio_inicio = fields.Date(string="Año de Inicio")
    estado = fields.Char(string="Estado", size=50)
    
    peliculas_ids= fields.One2many("upomax.pelicula","nombre_franquicia_id",string="Peliculas confirmadas")

    peliculas_count = fields.Integer(
        string="Nº Películas", 
        compute='_compute_conteo', 
        store=True
    )
    @api.depends("peliculas_ids","series_ids")
    def _compute_conteo(self):
        for record in self:
            record.peliculas_count=len(record.peliculas_ids)
           
