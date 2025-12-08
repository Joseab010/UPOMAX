from odoo import models, fields

class Lista(models.Model):
    _name = 'upomax.lista'
    _description = 'Lista de Usuarios'
    
    name = fields.Char(string="Nombre de la Lista", required=True)
    descripcion = fields.Text(string="Descripción")
    
    usuario_id = fields.Many2one('upomax.usuario', string="Usuario", required=True)
    
    pelicula_ids = fields.Many2many(
        'upomax.pelicula', 
        'rel_lista_pelicula', 
        'lista_id', 
        'pelicula_id',
        string="Películas"
    )
    
    serie_ids = fields.Many2many(
        'upomax.serie',
        'rel_lista_serie',
        'lista_id',
        'serie_id',
        string="Series"
    )
