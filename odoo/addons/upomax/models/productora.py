from odoo import models, fields, api

class productora(models.Model):
    _name = 'upomax.productora'
    _description = 'Productora'

    name = fields.Char(string="Nombre de la Productora", required=True, size=100)
    
    fundacion = fields.Date(string="Fecha de Fundación")
    pais = fields.Char(string="País", size=50)

    peliculas_ids = fields.Many2many(
        'upomax.pelicula',          
        'rel_productora_pelicula',      
        'productora_id',                
        'pelicula_id',              
        string="Peliculas confirmadas"
    )

    peliculas_count = fields.Integer(
        string="Nº Películas", 
        compute='_compute_conteo', 
        store=True
    )
    
    @api.depends("peliculas_ids")
    def _compute_conteo(self):
        for record in self:
            record.peliculas_count=len(record.peliculas_ids)

    #Validación duplicidad nombre productora
    @api.constrains('name')
    def _check_nombre_unico(self):
        for rec in self:
            domain = [
                ('name', '=ilike', rec.name),
                ('id', '!=', rec.id) # Q no sea el mismo
            ]
            if self.search_count(domain) > 0:
                raise ValidationError(f"La productora '{rec.name}' ya existe en la base de datos.")

    # Comprueba que ninguna película sea anterior a la fundación de la productora
    @api.constrains('fundacion', 'peliculas_ids')
    def _check_coherencia_peliculas(self):
        for rec in self:
            if rec.fundacion and rec.peliculas_ids:
                for peli in rec.peliculas_ids:
                    # Campo anio
                    if peli.anio and peli.anio < rec.fundacion:
                        raise ValidationError(
                            f"Incoherencia temporal detectada:\n"
                            f"- La película '{peli.name}' se estrenó el {peli.anio}.\n"
                            f"- Pero la productora '{rec.name}' no se fundó hasta el {rec.fundacion}.\n"
                        )