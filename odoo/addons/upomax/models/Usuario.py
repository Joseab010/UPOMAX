from odoo import models, fields, api


class Usuario(models.Model):
    _name = 'upomax.usuario'
    _description = 'Tabla con informacion de los usuarios'
    
    name = fields.Char(string="nombre usuario", required=True,size=100, help="Nombre de Usuario")
    Correo_Electronico = fields.Char(string="correo_electronico", size=100,required=True, help="Nombre de Correo")
    Contraseña = fields.Char(string="correo_electronico", size=100,required=True, help="Contraseña usuario")
    biografia = fields.Char(string="biografia", size=100,required=True, help="biografia de usuario")
