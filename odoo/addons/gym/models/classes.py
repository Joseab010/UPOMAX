# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Classes(models.Model):
     _name = 'gym.classes'
     _description = 'Gym Classes'

     name = fields.Char(string="Title", required=True, help="name of the gym")
     description = fields.Text()
     start = fields.Datetime('Starts',required=True, autodate = True)
     end = fields.Datetime('Ends',required=True, autodate = True)
     capacity = fields.Integer("Capacity") 
     activityType = fields.Selection([('dance','Dance'),
                                     ('aerobic','Aerobic'),
                                     ('anaerobic','Anaerobic'),
                                     ('relax','Relax'),],
                                     'Type of activity')
     users_ids = fields.Many2many("gym.users",string="Confirmed users")
     instructores_id=fields.Many2one('gym.instructores',string="Instructor")