from odoo import models, fields, api

class Pelicula(models.Model):
    _name = 'upomax.pelicula'
    _description = 'Película'

    name = fields.Char(string="Título", required=True, size=100)
    _sql_constraints = [
        ('titulo_unique', 'UNIQUE(titulo)', 'El título de la película debe ser único.')
    ]
    descripcion = fields.Text(string="Descripción", size=500)
    puntuacion_general = fields.Float(string="Puntuación General", digits=(2, 2))
    anio = fields.Date(string="Año de Estreno")
    edad_recomendada = fields.Integer(string="Edad Recomendada")
    duracion = fields.Integer(string="Duración (minutos)")
    nombre_productora_id = fields.Many2one('upomax.productora', string='Productora', size=100)