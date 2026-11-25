# from odoo import http


# class Autofix(http.Controller):
#     @http.route('/autofix/autofix', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/autofix/autofix/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('autofix.listing', {
#             'root': '/autofix/autofix',
#             'objects': http.request.env['autofix.autofix'].search([]),
#         })

#     @http.route('/autofix/autofix/objects/<model("autofix.autofix"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('autofix.object', {
#             'object': obj
#         })

