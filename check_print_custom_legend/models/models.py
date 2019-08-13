# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class check_print_custom_legend(models.Model):
#     _name = 'check_print_custom_legend.check_print_custom_legend'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100