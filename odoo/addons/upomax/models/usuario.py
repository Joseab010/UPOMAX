from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re    #para las expresiones regulares

class Usuario(models.Model):
    _name = 'upomax.usuario'
    _description = 'Tabla con informacion de los usuarios'
    
    name = fields.Char(string="Nombre usuario", required=True,size=100, help="Nombre de Usuario")
    correo_Electronico = fields.Char(string="Correo electronico", size=100,required=True, help="Nombre de Correo")
    contrasenya = fields.Char(string="Contraseña", size=100,required=True, help="Contraseña usuario")
    biografia = fields.Char(string="biografia", size=400, help="biografia de usuario")


    reviews_ids = fields.One2many('upomax.review',inverse_name='id_usuario',string="Reseñas de usuarios")
    
    amigos_ids = fields.Many2many('upomax.usuario',
                                  'rel_usuario_amistad',
                                  'usuario_id',
                                  'amigo_id',
                                  string="Lista de amigos")
    
    #Validacion para el nombre
    @api.constrains('name')
    def _check_name(self):
        for rec in self:
            if not rec.name or len(rec.name.strip()) < 3:
                raise ValidationError("El nombre debe tener al menos 3 caracteres.")
            if not re.match(r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]+$', rec.name):
                raise ValidationError("El nombre solo puede contener letras y espacios.")      
    
    #Validacion para el correo
    @api.constrains('correo_Electronico')
    def _check_email(self):
        for rec in self:
            if not rec.correo_Electronico:
                raise ValidationError("El correo no puede estar vacio.")
            if not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', rec.correo_Electronico):
                raise ValidationError("El email no cumple el formato.") 
    
    #Validacion para password    
    @api.constrains('contrasenya')     
    def _check_password(self):         
        for rec in self:             
            if not rec.contrasenya:            
                raise ValidationError("La contraseña no puede estar vacia.")           
            if not re.match(r'^(?=(?:.*\d){4,})(?=.*[a-z])(?=.*[A-Z]).*$', rec.contrasenya):        
                raise ValidationError("La contraseña no cumple el formato debe contener al menos una mayuscula, una minuscula y 4 dígitos.") 

    #Validacion para biografia    
    @api.constrains('biografia')     
    def _check_password(self):         
        for rec in self:             
            if rec.biografia and len(rec.biografia)>400:      
                raise ValidationError(f"La biografía es demasiado larga. Tienes {len(rec.biografia)} caracteres, pero el límite es 400.")