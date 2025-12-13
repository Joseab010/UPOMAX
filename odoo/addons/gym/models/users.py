# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class Users(models.Model):
     _name = 'gym.users'
     _description = 'Gym Users'

     name = fields.Char(string="First name", size=60, required=True, help="Name of the user")
     idcard = fields.Char('ID Card', size=9, required=True)
     photo=fields.Binary('Photo')
     state = fields.Selection([('solicitante','Solicitante'),
                                     ('admitido','Admitido'),
                                     ('cancelado','Cancelado'),],
                                     'Estado', default='solicitante')
     classes_ids = fields.Many2many("gym.classes",string="Confirmed classes")

     _sql_constraints = [('users_idcard_unique','UNIQUE (idcard)','El idcard debe ser único')]
     
     def action_print_class(self):
          self.ensure_one()
          report = self.env.ref('gym.action_gym_users_report', raise_if_not_found=False)
          if not report:
               report = self.env['ir.actions.report'].search(
                    [('report_name', '=', 'gym.gym_users_template')], limit=1
               )
          if not report:
               from odoo.exceptions import UserError
               raise UserError(
                    "No se encontró la acción de informe 'gym.action_gym_users_report' "
                    "ni un reporte con report_name='gym.gym_users_template'."
               )
          return report.report_action(self)

     def btn_submit_to_admitido(self):
          self.write({'state':'admitido'})

     def btn_submit_to_cancelado(self):
          self.write({'state':'cancelado'})

          # Hay que borrar todas las clases reservadas
          # para fechas posteriores al momento de la cancelacion
          hoy = fields.Datetime.now()

          for clase in self.classes_ids:
               if clase.start > hoy:
                    self.write({'classes_ids':[(3,clase.id)]})

     def btn_submit_to_solicitado(self):
          self.write({'state':'solicitante'})
     
     @api.onchange('classes_ids')
     def onchange_classes(self):
          if self.idcard != False and self.state != 'admitido': # el false de idcard sirve para que no se ejecute el onchange al pulsar el boton "Create"
               raise ValidationError('El usuario debe estar admitido para apuntarlo a una clase')

     
