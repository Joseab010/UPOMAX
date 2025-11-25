from pydantic import ValidationError
from odoo import models, fields, api


class Review(models.Model):
    _name = 'upomax.review'
    _description = 'Tabla con informacion de las review'
    
    name = fields.Integer(string="id review",required=True)
    
    titulo = fields.Char(string="Titulo de la review",required=True,size=100)
    
    calificacion= fields.Integer(string="calificacion",required=True)
    
    comentario= fields.Char(string="comentario de la pelicula",size=500)
    
    fecha =fields.Date(string="fecha de publicacion")
    
    like = fields.Boolean(string="Me gusta")


    # Validacion para la calificacion
    @api.constrains('calificacion')
    def _check_calificacion(self):
        for rec in self:
            if rec.calificacion < 1 or rec.calificacion > 5:
                raise ValidationError("La calificación debe estar entre 1 y 5.")
            if not isinstance(rec.calificacion, int):
                raise ValidationError("La calificación debe ser un número entero.")
            

    # Relaciones
    id_usuario = fields.Many2one('upomax.usuario',string="Usuario que hizo la review", required=True)
    
    serie_id = fields.Many2one('upomax.serie',string="Serie reseñada")

    pelicula_id = fields.Many2one('upomax.pelicula', string="Pelicula reseñada")

    
    