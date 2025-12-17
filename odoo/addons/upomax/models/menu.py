# -*- coding: utf-8 -*-

from odoo import models, api

class MainMenu(models.TransientModel):
    _name = 'upomax.main_menu'
    _description = 'UPOMAX Main Menu'

    def action_series(self):
        return self.env.ref('upomax.serie_list_action').read()[0]

    def action_peliculas(self):
        return self.env.ref('upomax.peliculas_list_action').read()[0]

    def action_plataformas(self):
        return self.env.ref('upomax.plataforma_list_action').read()[0]

    def action_personas(self):
        return self.env.ref('upomax.personas_list_action').read()[0]

    def action_reviews(self):
        return self.env.ref('upomax.review_list_action').read()[0]

    def action_usuarios(self):
        return self.env.ref('upomax.usuario_list_action').read()[0]