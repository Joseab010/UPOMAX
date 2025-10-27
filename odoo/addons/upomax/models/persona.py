# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Persona(models.Model):
    _name = 'upomax.persona'


    nombre = fields.Char(string="Nombre", required=True, size=50)
    
  
    apellidos = fields.Char(string="Apellidos", size=50)
    
 
    edad = fields.Integer(string="Edad")

    biografia = fields.Text(string="Biografía", size=300)
