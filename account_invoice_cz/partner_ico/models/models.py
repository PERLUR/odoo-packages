# -*- coding: utf-8 -*-

from odoo import models, fields, api, time


class ResPartner(models.Model):
    _inherit = 'res.partner'

    ico = fields.Char('IČ')

    @api.model
    def _ico(self):
        return super(ResPartner, self)._ico() + ['ico']


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def _default_date_zdpl(self):
        return time.strftime('%Y-%m-%d')

    date_zdpl = fields.Date(string='DUZP', readonly=True, states={'draft': [(
        'readonly', False)]}, help="Datum uskutečnění zdanitelného plnění", default=_default_date_zdpl)

    @api.model
    def _date_zdpl(self):
        return super(AccountInvoice, self)._date_zdpl() + ['date_zdpl']


class ResCompany(models.Model):
    _inherit = 'res.company'

    ico = fields.Char('IČ')

    @api.model
    def _ico(self):
        return super(ResCompany, self)._ico() + ['ico']