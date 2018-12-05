# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    company_registry = fields.Char('Company Registry')

    @api.model
    def _company_registry(self):
        return super(ResPartner, self)._company_registry() + ['company_registry']

