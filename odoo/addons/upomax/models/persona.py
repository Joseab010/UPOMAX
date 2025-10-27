# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Persona(models.Model):
    _name = 'upomax.persona'


    nombre = fields.Char(string="Nombre", required=True)
    
  
    apellidos = fields.Char(string="Apellidos")
    
 
    edad = fields.Integer(string="Edad")

    biografia = fields.Text(string="Biografía")
