from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Tracks(models.Model):
    _name = 'upomax.track'
    _description = 'Tabla con informacion de los tracks'
    
    name = fields.Char(string="Titulo", size=100,required=True)
    duracion = fields.Integer(string="Duracion (min)") 
    capitulo_id = fields.Many2one('upomax.capitulo',inverse_name= "tracks_ids" ,string='Capitulo')

    
    banda_sonora_id = fields.Many2many('upomax.banda.sonora',
                          'rel_banda_sonora_tracks',
                          'tracks_id',
                          'banda_sonora_id',
                          string='Banda sonora incluidas')
    
    @api.constrains("duracion")
    def _check_duracion(self):
        if self.duracion<0:
            raise ValidationError("La duración no puede ser Negativa")
        
    #impedir capítulos huérfanos
    @api.constrains('capitulo_id', 'banda_sonora_id')
    def _check_track_huerfano(self):
        for rec in self:
            if not rec.capitulo_id and not rec.banda_sonora_id:
                raise ValidationError("El track debe estar vinculado a un Capítulo o a una Banda Sonora. No puede quedar flotando en el sistema.")
    
    #Valiación de duplicados en el mismo capítulo
    @api.constrains('name', 'capitulo_id')
    def _check_duplicado_en_capitulo(self):
        for rec in self:
            if rec.capitulo_id:
                domain = [
                    ('name', '=ilike', rec.name),          
                    ('capitulo_id', '=', rec.capitulo_id.id),
                    ('id', '!=', rec.id)                  
                ]
                if self.search_count(domain) > 0:
                    raise ValidationError(f"El track '{rec.name}' ya existe en el capítulo seleccionado.")
                
    @api.constrains('name')
    def _check_nombre_calidad(self):
        for rec in self:
            if len(rec.name.strip()) < 3:
                raise ValidationError("El título del track es demasiado corto. Debe tener al menos 3 caracteres.")