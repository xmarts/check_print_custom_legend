# -*- coding: utf-8 -*-
from odoo import http

# class CheckPrintCustomLegend(http.Controller):
#     @http.route('/check_print_custom_legend/check_print_custom_legend/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/check_print_custom_legend/check_print_custom_legend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('check_print_custom_legend.listing', {
#             'root': '/check_print_custom_legend/check_print_custom_legend',
#             'objects': http.request.env['check_print_custom_legend.check_print_custom_legend'].search([]),
#         })

#     @http.route('/check_print_custom_legend/check_print_custom_legend/objects/<model("check_print_custom_legend.check_print_custom_legend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('check_print_custom_legend.object', {
#             'object': obj
#         })