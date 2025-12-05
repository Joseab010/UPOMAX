from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

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
    
    @api.depends("peliculas_ids")
    def _compute_conteo(self):
        for record in self:
            record.peliculas_count=len(record.peliculas_ids)
           
    @api.constrains('anio_inicio')
    def _check_anio_inicio(self):
        current_year = datetime.now().year
        for rec in self:
            if rec.anio_inicio:
                anio = rec.anio_inicio.year 
                if anio < 1895:
                    raise ValidationError("El cine se inventó en 1895. La franquicia no puede ser anterior.")
                if anio > current_year + 5:
                    raise ValidationError("La fecha de inicio es demasiado lejana en el futuro.")