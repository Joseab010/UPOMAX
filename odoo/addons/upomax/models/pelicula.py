from odoo import models, fields, api

class Pelicula(models.Model):
    _name = 'upomax.pelicula'
    _description = 'Película'

    name = fields.Char(string="Título", required=True, size=100)
    
    descripcion = fields.Text(string="Descripción", size=500)
    puntuacion_general = fields.Float(string="Puntuación General", digits=(2, 2))
    anio = fields.Date(string="Año de Estreno")
    edad_recomendada = fields.Integer(string="Edad Recomendada")
    duracion = fields.Integer(string="Duración (minutos)")
    
    plataformas_ids= fields.Many2many("upomax.plataforma",string="Plataformas confirmadas")
    nombre_franquicia_id = fields.Many2one('upomax.franquicia', string='Franquicia')
    nombre_banda_id = fields.Many2one('upomax.banda.sonora', string='Banda Sonora') 
    
    
    generos_ids = fields.Many2many(
        'upomax.genero',           
        'rel_genero_pelicula',        
        'pelicula_id',               
        'genero_id',               
        string="Géneros"
    )

    productoras_ids = fields.Many2many(
        'upomax.productora',           
        'rel_productora_pelicula',        
        'pelicula_id',               
        'productora_id',               
        string="Productoras"
    )

    premios_ids = fields.One2many('upomax.premio',inverse_name='titulo_pelicula',string='Premios') #on2many obligatorio inversename

    reviews_ids=fields.One2many('upomax.review',inverse_name='pelicula_id',string='Reseñas')
    
    personas_ids = fields.Many2many('upomax.tipo', 
                                    'rel_pelicula_persona', 
                                    'pelicula_id',
                                    'persona_tipo_id',
                                    string="Persona con participación específica",
                                    required=True)