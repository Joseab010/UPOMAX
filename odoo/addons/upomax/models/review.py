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


    id_usuario = fields.Many2one('upomax.usuario',string="Usuario que hizo la review", required=True)
    
    serie_id = fields.Many2one('upomax.serie',string="Serie reseñada")

    pelicula_id = fields.Many2one('upomax.pelicula', string="Pelicula reseñada")

    
    