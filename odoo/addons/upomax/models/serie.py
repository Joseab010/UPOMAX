from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Serie(models.Model):
    _name = 'upomax.serie'
    _description = 'Tabla con informacion de las series'

    name = fields.Char(string="Titulo", required=True, size=100)
    fecha_emision = fields.Date(string="Fecha de emision")
    fecha_finalizacion = fields.Date(string="Fecha de finalizacion")
    duracion = fields.Integer(string="Duración (min)")
    edad_recomendada = fields.Integer(string="Edad Recomendada")
    
    image = fields.Image(string="Carátula", max_width=1024, max_height=1024)

    puntuacion_general = fields.Float(
        string="Puntuación General", 
        digits=(2, 2), 
        compute='_compute_puntuacion_general', 
        store=True
    )

    plataformas_ids = fields.Many2many(
        'upomax.plataforma',
        'rel_plataforma_serie',
        'serie_id',
        'plataforma_id',
        string="Plataformas confirmadas"
    )
    
    generos_ids = fields.Many2many(
        'upomax.genero',          
        'rel_genero_serie',       
        'serie_id',               
        'genero_id',              
        string="Géneros"
    )
    
    # Relaciones One2many
    temporadas_ids = fields.One2many('upomax.temporada', inverse_name='serie_id', string='Temporada')
    premios_ids = fields.One2many('upomax.premio', inverse_name='titulo_serie', string='Premios')
    reviews_ids = fields.One2many('upomax.review', inverse_name='serie_id', string='Reseñas')
    participacion_ids = fields.One2many('upomax.persona.tipo', 'serie_id', string="Participaciones")
    
    # Campos filtrados para vistas (Directores, Actores, etc)
    directores_ids = fields.One2many(
        'upomax.persona.tipo', 
        'serie_id', 
        domain=[('tipo_id.name', '=', 'Director')],
        string="Directores"
    )
    actores_ids = fields.One2many(
        'upomax.persona.tipo', 
        'serie_id', 
        domain=[('tipo_id.name', '=', 'Actor')],
        string="Actores"
    )
    compositores_ids = fields.One2many(
        'upomax.persona.tipo', 
        'serie_id', 
        domain=[('tipo_id.name', '=', 'Compositor')],
        string="Compositores"
    )

    @api.constrains("duracion")
    def _check_duracion(self):
        for record in self:
            if record.duracion < 0:
                raise ValidationError("La duración no puede ser negativa")

    @api.depends('reviews_ids.calificacion')   
    def _compute_puntuacion_general(self):
        for serie in self:
            if serie.reviews_ids:
                calificaciones = [r.calificacion for r in serie.reviews_ids]
                promedio = sum(calificaciones) / len(calificaciones)
                serie.puntuacion_general = promedio
            else:
                serie.puntuacion_general = 0.0

    @api.constrains('fecha_emision', 'fecha_finalizacion')
    def _check_fechas_coherentes(self):
        for rec in self:
            if rec.fecha_emision and rec.fecha_finalizacion:
                if rec.fecha_finalizacion < rec.fecha_emision:
                    raise ValidationError("La fecha de finalización no puede ser anterior a la fecha de emisión.")

    @api.constrains('name', 'fecha_emision')
    def _check_nombre_emision_unico(self):
        for rec in self:
            if rec.name and rec.fecha_emision:
                domain = [
                    ('name', '=', rec.name),
                    ('fecha_emision', '=', rec.fecha_emision),
                    ('id', '!=', rec.id)
                ]
                if self.search_count(domain) > 0:
                    raise ValidationError(f"Ya existe la serie '{rec.name}' con esa fecha de emisión.")
      
    @api.constrains("name")
    def _check_name(self):
        for record in self:
            if not record.name or len(record.name.strip()) < 3:
                raise ValidationError("El nombre debe tener al menos 3 caracteres.")
            if not re.match(r'^[a-zA-Z0-9áéíóúüñÁÉÍÓÚÜÑ\s\.,:;!?\-\(\)\'"&]+$', record.name):
                raise ValidationError("El nombre contiene caracteres no válidos.")

    @api.constrains('edad_recomendada')
    def _check_edad_recomendada(self):
        for rec in self:
            if rec.edad_recomendada < 0:
                raise ValidationError("La edad recomendada no puede ser negativa.")
            if rec.edad_recomendada > 18:
                raise ValidationError("La clasificación por edades estándar llega hasta 18 años.")
    
    @api.constrains('generos_ids')
    def _check_tiene_generos(self):
        for rec in self:
            if not rec.generos_ids:
                raise ValidationError("La serie debe tener clasificado al menos un Género.")