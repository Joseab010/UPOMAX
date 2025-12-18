# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class Classes(models.Model):
     _name = 'gym.classes'
     _description = 'Gym Classes'

     name = fields.Char(string="Title", required=True, help="name of the gym")
     description = fields.Text()
     start = fields.Datetime('Starts', autodate = True)
     end = fields.Datetime('Ends', autodate = True)
     capacity = fields.Integer("Capacity") 
     activityType = fields.Selection([('dance','Dance'),
                                     ('aerobic','Aerobic'),
                                     ('anaerobic','Anaerobic'),
                                     ('relax','Relax'),],
                                     'Type of activity')
     users_ids = fields.Many2many("gym.users",string="Confirmed users")
     instructores_id=fields.Many2one('gym.instructores',string="Instructor")
     ocupacion = fields.Integer(compute='_ocupacionTotal',string='Ocupacion total',store=True)
     
     def action_print_class(self):
          self.ensure_one()
          report = self.env.ref('gym.action_gym_classes_report', raise_if_not_found=False)
          if not report:
               report = self.env['ir.actions.report'].search(
                    [('report_name', '=', 'gym.gym_classes_template')], limit=1
               )
          if not report:
               raise UserError(
                    "No se encontró la acción de informe 'gym.action_gym_classes_report' "
                    "ni un reporte con report_name='gym.gym_classes_template'."
               )
          return report.report_action(self)
               
     def btn_desapuntarSocios(self):
          self.write({'users_ids':[(5,)]})
     
     @api.depends('users_ids')
     def _ocupacionTotal(self): 
          for record in self:                            
               record.ocupacion = len(record.users_ids)

     @api.constrains('capacity')
     def _check_capacity(self):
          if self.capacity >= 50:
               raise ValidationError('La capacidad de la clase debe ser inferior a 50.')
     
     @api.onchange('capacity','activityType')
     def onchange_classes(self):
          resultado = {}
          if self.capacity >= 30 and self.activityType == 'dance':
               resultado = {
                    'value': {'capacity':30},
                    'warning': {
                         'title':'Valores incorrectos',
                         'message':'Las clases de baile son para maximos 30 personas'
                    }
               }
               return resultado