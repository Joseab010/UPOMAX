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