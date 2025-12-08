from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Persona(models.Model):
    _name = 'upomax.persona'
    _description = "Persona"
    _rec_name = 'nombre'  # Para que al buscar aparezca el nombre, no el ID
 
 
    nombre = fields.Char(string="Nombre", required=True, size=50)
    apellidos = fields.Char(string="Apellidos", size=50)
    
    edad = fields.Integer(string="Edad")
    biografia = fields.Text(string="Biografía")

    participacion_ids = fields.One2many(
        'upomax.persona.tipo', 
        'persona_id', 
        string="Participaciones en películas/series"
    )

    tipos_ids = fields.Many2many(
        'upomax.tipo',
        'rel_persona_tipo',
        'persona_id',
        'tipo_id',
        string="Roles disponibles"
    )
    
    @api.constrains('edad')
    def _check_age(self):
        for rec in self:
            if rec.edad < 0:
                raise ValidationError("La edad no puede ser negativa.")
            if rec.edad > 120:
                raise ValidationError("La edad no puede ser mayor a 120 años.")
    
    @api.constrains('biografia')
    def _check_biografia(self):
        for rec in self:
            if rec.biografia and len(rec.biografia) > 300:
                raise ValidationError(f"La biografía es demasiado larga ({len(rec.biografia)} car.), límite 300.")

    @api.constrains('nombre', 'apellidos')
    def _check_nombres(self):
        for rec in self:
            pattern = r'^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]+$'
            if rec.nombre and not re.match(pattern, rec.nombre):
                raise ValidationError("El nombre solo puede contener letras y espacios.")
            if rec.apellidos and not re.match(pattern, rec.apellidos):
                raise ValidationError("Los apellidos solo pueden contener letras y espacios.")            