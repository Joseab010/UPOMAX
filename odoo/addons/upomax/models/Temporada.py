from odoo import models, fields, api


class temporada(models.Model):
    _name = 'upomax.temporada'
    _description = 'Tabla con informacion de las premios'


    name = fields.Char(
        string="Título de la Temporada", 
        required=True, 
        size=100,
        help="Ej: 'Temporada 1' "
    )

    num_temporada = fields.Integer(string="Número de Temporada", required=True)
    
    cantidad_capitulos = fields.Integer(string="Cantidad de Capítulos", compute="_compute_cantidad_capitulos", store=True)

    serie_id = fields.Many2one('upomax.serie',
                               string='Serie')
    
    capitulo_ids = fields.One2many('upomax.capitulo',
                                   'temporada_id',
                                   string='Capítulos de la Temporada')
    
    @api.depends('capitulo_ids')
    def _compute_cantidad_capitulos(self):
        for record in self:
            record.cantidad_capitulos = len(record.capitulo_ids)

    
    #validación unicidad temporada por serie
    @api.constrains('serie_id', 'num_temporada')
    def _check_temporada_duplicada(self):
        for rec in self:
            if rec.serie_id and rec.num_temporada:
                domain = [
                    ('serie_id', '=', rec.serie_id.id),
                    ('num_temporada', '=', rec.num_temporada),
                    ('id', '!=', rec.id)  # Excluimos el registro que estamos editando
                ]
                if self.search_count(domain) > 0:
                    raise ValidationError(f"La serie '{rec.serie_id.name}' ya tiene registrada la Temporada {rec.num_temporada}.")

    #Validación numérica lógica
    @api.constrains('num_temporada')
    def _check_numero_logico(self):
        for rec in self:
            if rec.num_temporada < 1:
                raise ValidationError("El número de temporada debe ser 1 o superior.") 
            
    @api.constrains('serie_id')
    def _check_serie_obligatoria(self):
        for rec in self:
            if not rec.serie_id:
                raise ValidationError("Toda temporada debe pertenecer a una Serie. El campo no puede estar vacío.")
    
    #Validación calidad nombre temporada
    @api.constrains('name')
    def _check_nombre_calidad(self):
        for rec in self:
            if len(rec.name.strip()) < 3:
                raise ValidationError("El título de la temporada es demasiado corto. Sé más descriptivo.")