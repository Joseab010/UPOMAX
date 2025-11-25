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
    
    like = fields.Boolean(string="Me gusta", required=True, default=None)

    # Validacion para el titulo
    @api.constrains('titulo')
    def _check_titulo(self):
        for rec in self:
            if not rec.titulo or len(rec.titulo.strip()) < 5:
                raise ValidationError("El título debe tener al menos 5 caracteres.")

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

    # Validacion para que la review este asociada a una serie o pelicula pero no a ambas
    @api.constrains('serie_id', 'pelicula_id')
    def _check_serie_or_pelicula(self):
        for rec in self:
            if not rec.serie_id and not rec.pelicula_id:
                raise ValidationError("La review debe estar asociada a una serie o a una película.")
            if rec.serie_id and rec.pelicula_id:
                raise ValidationError("La review no puede estar asociada a una serie y a una película al mismo tiempo.")

    # Validacion para el like
    @api.constrains('like')
    def _check_like(self):
        for rec in self:
            if rec.like is None:
                raise ValidationError("Debes indicar si te gusta o no.")
