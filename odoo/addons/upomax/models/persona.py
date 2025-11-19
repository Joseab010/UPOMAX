# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Persona(models.Model):
    _name = 'upomax.persona'
    _description= "Persona"

    name = fields.Integer(string="Id")

    nombre = fields.Char(string="Nombre", required=True, size=50)
      
    apellidos = fields.Char(string="Apellidos", size=50)

    edad = fields.Integer(string="Edad")

    biografia = fields.Text(string="Biografía", size=300)


   

    tipos_ids = fields.Many2Many('upomax.tipo', #tabla a la que va
                                 'rel_persona_tipo', #tabla intermedia
                                 'persona_id', #primer id
                                 'tipo_id', #segundo id
                                 string="Tipos de Persona. Papel que desempeña")