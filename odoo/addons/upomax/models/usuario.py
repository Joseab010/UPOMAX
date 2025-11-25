from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re    #para las expresiones regulares

class Usuario(models.Model):
    _name = 'upomax.usuario'
    _description = 'Tabla con informacion de los usuarios'
    
    name = fields.Char(string="nombre usuario", required=True,size=100, help="Nombre de Usuario")
    correo_Electronico = fields.Char(string="correo_electronico", size=100,required=True, help="Nombre de Correo")
    contrasenya = fields.Char(string="Contraseña", size=100,required=True, help="Contraseña usuario")
    biografia = fields.Char(string="biografia", size=100, help="biografia de usuario")


    reviews_ids = fields.One2many('upomax.review',inverse_name='id_usuario',string="Reseñas de usuarios")
    
    amigos_ids = fields.Many2many('upomax.usuario',
                                  'rel_usuario_amistad',
                                  'usuario_id',
                                  'amigo_id',
                                  string="Lista de amigos")

    def _check_name(self):
        for rec in self:
            if not rec.name or len(rec.name.strip()) < 3:
                raise ValidationError("El nombre debe tener al menos 3 caracteres.")
            if not re.match(r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]+$', rec.name):
                raise ValidationError("El nombre solo puede contener letras y espacios.")      
            