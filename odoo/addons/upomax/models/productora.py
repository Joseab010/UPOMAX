from odoo import models, fields, api

class productora(models.Model):
    _name = 'upomax.productora'
    _description = 'Productora'

    name = fields.Char(string="Nombre de la Productora", required=True, size=100)
    
    fundacion = fields.Date(string="Fecha de Fundación")
    pais = fields.Char(string="País", size=50)

    peliculas_ids = fields.Many2many(
        'upomax.pelicula',          
        'rel_productora_pelicula',      
        'productora_id',                
        'pelicula_id',              
        string="Peliculas confirmadas"
    )