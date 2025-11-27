# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Persona(models.Model):
    _name = 'upomax.persona'
    _description= "Persona"

    name = fields.Integer(string="Id")

    nombre = fields.Char(string="Nombre", required=True, size=50)
      
    apellidos = fields.Char(string="Apellidos", size=50)

    edad = fields.Integer(string="Edad")

    biografia = fields.Text(string="Biografía", size=300)

    participacion_ids = fields.One2many('upomax.persona.tipo', 'persona_id', string="Participaciones en películas/series")

    tipos_ids = fields.Many2many('upomax.tipo',
                                 'rel_persona_tipo',
                                 'persona_id',
                                 'tipo_id',
                                 string="Roles disponibles")
    
    
    @api.constrains('edad')
    def _check_age(self):  
     if self.edad < 0:
       raise ValidationError("La edad no puede ser negativa.")
     
     #Validacion para biografia    
    @api.constrains('biografia')     
    def _check_password(self):         
        for rec in self:             
            if rec.biografia and len(rec.biografia)>300:      
                raise ValidationError(f"La biografía es demasiado larga. Tienes {len(rec.biografia)} caracteres, pero el límite es 300.")