# -*- coding: utf-8 -*-
from odoo import http

# class WProductionWason(http.Controller):
#     @http.route('/w_production_wason/w_production_wason/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/w_production_wason/w_production_wason/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('w_production_wason.listing', {
#             'root': '/w_production_wason/w_production_wason',
#             'objects': http.request.env['w_production_wason.w_production_wason'].search([]),
#         })

#     @http.route('/w_production_wason/w_production_wason/objects/<model("w_production_wason.w_production_wason"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('w_production_wason.object', {
#             'object': obj
#         })