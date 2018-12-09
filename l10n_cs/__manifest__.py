# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2012 - 2018 PERLUR Group (<https://go.perlur.cloud/opensource>).
#    Copyright (C) 2018 Optimal 4 s.r.o. (<https://www.optimal4.cz>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Czech - Accounting',
    'version': '2.1',
    'category': 'Accounting',
    'description': """
This is the latest Czech Odoo (OpenERP) localisation necessary to run Odoo accounting for Czech businesses with:
============================================================================================================
    - a Chart Of Accounts for Czech Republic
    - VAT tax structure with VATs for years 2018
    - a few other adaptations""",
    'author': 'PERLUR Group and Optimal4',
    'price': '100',
    'currency': 'EUR',
    'website': 'https://go.perlur.cloud/odoo-packages/',
    'depends': ['account', 'base_iban', 'base_vat', 'l10n_multilang', 'contacts'],
    'data': [
        'partner_view.xml',
        'data/account_type.xml',
        'data/account_template_entrepreneurs.xml',
        'data/account_tax_code.xml',
        'data/account_chart.xml',
        'data/account_tax.xml',
        'data/account_fiscal_templates.xml',
        'wizard/l10n_cs_wizard.xml',
    ],
    'demo' : ['demo/demo.xml'],
    "update_xml" : ['views/partner_view.xml'],
    'installable': 'True',
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
