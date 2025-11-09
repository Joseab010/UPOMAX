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
    