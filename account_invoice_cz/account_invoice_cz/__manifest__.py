# -*- coding: utf-8 -*-

{
    'name': 'Czech invoice',
    'version': '3.4',
    'category': 'Czech accounting',
    'summary': 'Account invoice',
    'description': """
Czech invoice pdf
""",
    'website': 'https://www.optimal4.cz',
    'depends': ['sale', 'account', 'base_vat', 'partner_ico'],
    'data': [
        #        'security/ir.model.access.csv',
        'views/account_invoice_cz.xml',
    ],
    'demo': [],
}
