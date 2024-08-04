# -*- coding: utf-8 -*-
# from odoo import http


# class VeterinaryV14(http.Controller):
#     @http.route('/veterinary_v14/veterinary_v14/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/veterinary_v14/veterinary_v14/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('veterinary_v14.listing', {
#             'root': '/veterinary_v14/veterinary_v14',
#             'objects': http.request.env['veterinary_v14.veterinary_v14'].search([]),
#         })

#     @http.route('/veterinary_v14/veterinary_v14/objects/<model("veterinary_v14.veterinary_v14"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('veterinary_v14.object', {
#             'object': obj
#         })
