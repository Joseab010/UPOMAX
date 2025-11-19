from odoo import models, fields, api


class Tipo(models.Model):
    _name = 'upomax.Tipo'
    _description = 'Tabla con informacion de los Tipo'

    # el tipo de persona se elegirá desde una lista fija de opciones
    name=fields.char(String="Tipo de persona",required=True)
    
    persona_id = fields.Many2many('upomax.persona',"rel_persona_tipo",'tipo_id','persona_id',string="Tipos de Persona. Papel que desempeña", required=True)

    pelicula_ids = fields.Many2many('upomax.pelicula', 'rel_pelicula_persona', 'tipo_id', 'pelicula_id', string="Películas en las que ha participado", required=True)

    capitulo_ids = fields.Many2many('upomax.capitulo', 'rel_capitulo_persona', 'tipo_id', 'capitulo_id', string="Capítulos en los que ha participado", required=True)
