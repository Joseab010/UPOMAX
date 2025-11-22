from odoo import models, fields, api

class genero(models.Model):
    _name = 'upomax.genero'
    _description = 'Género'

    name = fields.Char(string="Tipo de Género", required=True, size=100)

    series_ids = fields.Many2many(
        'upomax.serie',             
        'rel_genero_serie',         
        'genero_id',                
        'serie_id',                 
        string="Series confirmadas"
    ) 
    
    
    peliculas_ids = fields.Many2many(
        'upomax.pelicula',          
        'rel_genero_pelicula',      
        'genero_id',                
        'pelicula_id',              
        string="Películas confirmadas"
    )
    

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
    @api.depends("peliculas_ids","series_ids")
    def _compute_conteo(self):
        for record in self:
            record.peliculas_count = len(record.peliculas_ids)
            record.series_count = len(record.series_ids)

    