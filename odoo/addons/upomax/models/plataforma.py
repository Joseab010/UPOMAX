from odoo import models, fields, api

class plataforma(models.Model):
    _name = 'upomax.plataforma'
    _description = 'Plataforma'

    name = fields.Char(string="Nombre de la Plataforma", required=True, size=100)


    series_ids = fields.Many2many(
        'upomax.serie',
        'rel_plataforma_serie',
        'plataforma_id',
        'serie_id',
        string="Series confirmadas"
    ) 
    peliculas_ids= fields.Many2many("upomax.pelicula",
                                    "rel_plataforma_pelicula",
                                    "plataforma_id",
                                    "pelicula_id",
                                    string="Peliculas confirmadas") 
    
    series_count=fields.Integer(string="Nº Series",
                                compute= "_compute_conteo",
                                store=True)
    
    peliculas_count = fields.Integer(
        string="Nº Películas", 
        compute='_compute_conteo', 
        store=True
    )
    @api.depends("peliculas_ids","series_ids")
    def _compute_conteo(self):
        for record in self:
            record.peliculas_count=len(record.peliculas_ids)
            record.series_count=len(record.series_ids)
    
    # Validación unicidad nombre plataforma
    @api.constrains('name')
    def _check_nombre_unico(self):
        for rec in self:
            domain = [
                ('name', '=ilike', rec.name), 
                ('id', '!=', rec.id)        # Q no sea el mismo
            ]
            if self.search_count(domain) > 0:
                raise ValidationError(f"La plataforma '{rec.name}' ya existe. No crees duplicados.")
            
    # Validación calidad nombre plataforma
    @api.constrains('name')
    def _check_nombre_calidad(self):
        for rec in self:
            nombre = rec.name.strip()
            # Longitud mínima
            if len(nombre) < 2:
                raise ValidationError("El nombre es demasiado corto para una plataforma.")
            
            # No empezar por número
            if nombre[0].isdigit():
                raise ValidationError("El nombre de una plataforma no debería empezar por un número.")
            
            # Caracteres prohibidos
            forbidden = ['@', '$', '%', '/', '\\', '{', '}']
            if any(char in nombre for char in forbidden):
                raise ValidationError("El nombre contiene caracteres inválidos que no parecen un nombre comercial.")