from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Pelicula(models.Model):
    _name = 'upomax.pelicula'
    _description = 'Película'

    name = fields.Char(string="Título", required=True, size=100)
    
    descripcion = fields.Text(string="Descripción", size=500)
    puntuacion_general = fields.Float(string="Puntuación General", digits=(2, 2), compute='_compute_puntuacion_general', store=True)
    anio = fields.Date(string="Año de Estreno")
    edad_recomendada = fields.Integer(string="Edad Recomendada")
    duracion = fields.Integer(string="Duración (minutos)")
    
    plataformas_ids= fields.Many2many("upomax.plataforma",
                                      'rel_plataforma_pelicula',
                                      'pelicula_id',
                                      'plataforma_id',
                                       string="Plataformas confirmadas")
    
    nombre_franquicia_id = fields.Many2one('upomax.franquicia',inverse_name="peliculas_ids" ,string='Franquicia')
    nombre_banda_id = fields.Many2one('upomax.banda.sonora', inverse_name='peliculas_ids', string='Banda Sonora') 
    
    
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

    premios_ids = fields.One2many('upomax.premio',inverse_name='titulo_pelicula',string='Premios')

    reviews_ids=fields.One2many('upomax.review',inverse_name='pelicula_id',string='Reseñas')
    
    participacion_ids = fields.One2many('upomax.persona.tipo', 'pelicula_id', string="Participaciones (persona + rol)")
    
    
    @api.constrains('duracion')
    def _check_duracion(self):  
     if self.duracion < 0:
       raise ValidationError("La duración no puede ser negativa.")
   
   #Validacion para descripcion    
    @api.constrains('descripcion')     
    def _check_descripcion(self):         
        for rec in self:             
            if rec.descripcion and len(rec.descripcion)>500:      
                raise ValidationError(f"La descripción es demasiado larga. Tienes {len(rec.biografia)} caracteres, pero el límite es 500.")