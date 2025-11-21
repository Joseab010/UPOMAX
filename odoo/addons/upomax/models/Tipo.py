from odoo import models, fields, api


class Tipo(models.Model):
    _name = 'upomax.tipo'
    _description = 'Tabla con informacion de los Tipo'

    # el tipo de persona se elegirá desde una lista fija de opciones
    name=fields.Char(string="Tipo de persona",required=True)
    
    persona_ids = fields.Many2many('upomax.persona',"rel_persona_tipo",'tipo_id','persona_id',string="Personas con este tipo")
    
    participacion_ids = fields.One2many('upomax.persona.tipo', 'tipo_id', string="Participaciones usando este rol")
