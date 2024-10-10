# -*- coding: utf-8 -*-
# from odoo import http


# class Ctnews(http.Controller):
#     @http.route('/ctnews/ctnews', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ctnews/ctnews/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ctnews.listing', {
#             'root': '/ctnews/ctnews',
#             'objects': http.request.env['ctnews.ctnews'].search([]),
#         })

#     @http.route('/ctnews/ctnews/objects/<model("ctnews.ctnews"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ctnews.object', {
#             'object': obj
#         })

