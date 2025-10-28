# from odoo import http


# class Upomax(http.Controller):
#     @http.route('/upomax/upomax', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upomax/upomax/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('upomax.listing', {
#             'root': '/upomax/upomax',
#             'objects': http.request.env['upomax.upomax'].search([]),
#         })

#     @http.route('/upomax/upomax/objects/<model("upomax.upomax"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upomax.object', {
#             'object': obj
#         })

