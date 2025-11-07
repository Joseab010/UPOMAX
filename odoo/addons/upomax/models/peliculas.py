from odoo import models, fields, api

class Peliculas(models.Model):
    _name = 'upomax.peliculas'
    _description = 'Película'

    name = fields.Char(string="Título", required=True, size=100)
    
    descripcion = fields.Text(string="Descripción", size=500)
    puntuacion_general = fields.Float(string="Puntuación General", digits=(2, 2))
    anio = fields.Date(string="Año de Estreno")
    edad_recomendada = fields.Integer(string="Edad Recomendada")
    duracion = fields.Integer(string="Duración (minutos)")
    
    
    #<field name="nombre_productora_id" widget="many2many_tags" />

    plataformas_ids= fields.Many2many("upomax.plataforma",string="Plataformas confirmadas")
    nombre_franquicia_id = fields.Many2one('upomax.franquicia', string='Franquicia')