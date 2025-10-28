# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Users(models.Model):
     _name = 'gym.users'
     _description = 'Gym Users'

     name = fields.Char(string="First name", size=60, required=True, help="Name of the user")
     idcard = fields.Char('ID Card', size=9, required=True)
     photo=fields.Binary('Photo')
     classes_ids = fields.Many2many("gym.classes",string="Confirmed classes")