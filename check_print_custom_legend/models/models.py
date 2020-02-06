# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountJournalInherit(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_custom_legend = fields.Boolean(string="Usar leyenda personalizada?", default=False)
    custom_legend_text = fields.Text(string="Leyenda personalizada")

class ResPartnerBank(models.Model):
    _name = 'res.partner.bank'
    _inherit = 'res.partner.bank'

    clabe = fields.Char(string="CLABE")

# class ResBank(models.Model):
#     _name = 'res.bank'
#     _inherit = 'res.bank'
#
#     complete_name = fields.Text(string="Nombre completo")

class AddAmountToTextACPay(object):
	"""docstring for AddAmountToTextACPay"""
	_inherit = 'account.payment'
	
	amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True,
                                 help='Amount of the invoice in letter', store=True)

	@api.one
	@api.depends('amount')
	def _get_amount_to_text(self):
		self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount, 'MXN')