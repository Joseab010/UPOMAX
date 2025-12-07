from odoo import models, fields, api


class PersonaTipo(models.Model):
    _name = 'upomax.persona.tipo'
    _description = 'Participación de persona con rol en película/serie'

    persona_id = fields.Many2one('upomax.persona', string="Persona", required=True, ondelete='cascade')
    tipo_id = fields.Many2one('upomax.tipo', string="Rol/Tipo", required=True)
    
    pelicula_id = fields.Many2one('upomax.pelicula', string="Película")
    serie_id = fields.Many2one('upomax.serie', string="Serie")
    capitulo_id = fields.Many2one('upomax.capitulo', string="Capítulo")
    
    personaje = fields.Char(string="Personaje", size=100, help="Nombre del personaje interpretado")