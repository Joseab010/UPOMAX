from odoo import models, fields, api


class Premios(models.Model):
    _name = 'upomax.temporada'
    _description = 'Tabla con informacion de las premios'


    titulo_temporada = fields.Char(
        string="Título de la Temporada", 
        required=True, 
        size=100,
        help="Ej: 'Temporada 1' "
    )
    
   
    num_temporada = fields.Integer(
        string="Número de Temporada",
        required=True, 
        help="Ej: 1, 2, 3..."
    )
    

    cantidad_capitulos = fields.Integer(string="Cantidad de Capítulos")


    #titulo fkpk