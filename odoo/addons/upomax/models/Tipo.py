from odoo import models, fields, api


class Tipo(models.Model):
    _name = 'upomax.Tipo'
    _description = 'Tabla con informacion de los Tipo'


    id_tipo=fields.Integer(String="Tipo de persona",required=True)
    
    nombre_tipo=fields.char(String="Nombre del tipo",
                            size=50,
                            help="Ej: David")
    
    pelicula_ids = fields.Many2Many('upomax.pelicula',
                                    "rel_persona_pelicula",
                                    "persona_id",
                                    "pelicula_id",
                                    string="Pelciualas en las que ha participado")