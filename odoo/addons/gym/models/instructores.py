# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Instructores(models.Model):
     _name = 'gym.instructores'
     _description = 'Gym Instructores'

     name = fields.Char(string="First name", size=60, required=True, help="Name of the user")
     idcard = fields.Char('ID Card', size=9, required=True)
     photo=fields.Binary('Photo')
     classes_ids = fields.One2many("gym.classes",'instructores_id','Classes')