from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Banda_sonora(models.Model):
    _name = 'upomax.banda.sonora'
    _description = 'Tabla con informacion de las bandas sonoras'
    
    name = fields.Char(string="Nombre_BSO", required=True,size=100, help="Nombre de BSO")
    
   
    anyo = fields.Date(string="fecha de salida")
    pais = fields.Char(string="Pais", size=100)
    peliculas_ids= fields.One2many("upomax.pelicula","nombre_banda_id",string="Peliculas confirmadas")

    tracks_id=fields.Many2many("upomax.track",
                         "rel_banda_sonora_tracks",
                         "banda_sonora_id",
                         "tracks_id",
                         string="Tracks incluidos")
    
    @api.constrains('anyo')
    def _check_anyo(self):
        current_year = datetime.now().year
        for rec in self:
            if rec.anyo and not (1900 <= rec.anyo <= current_year):
                raise ValidationError(f"El año debe estar entre 1900 y {current_year}.")