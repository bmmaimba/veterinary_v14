# -*- coding: utf-8 -*-
# https://www.odoo.com/documentation/14.0/howtos/backend.html

{
    'name': "veterinary_v14",

    'summary': """
        veterinary_v14""",

    'description': """
        veterinary_v14
    """,

    'author': "Benjamin Maimba",
    'website': "http://www.datalynix.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Veterinary',
    'version': '14.4.6',
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base','calendar','account','sale','base_automation'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/customer_view.xml',
        'views/bill_view.xml',
        'views/invoice_view.xml',
        'views/vaccinations.xml',
        'views/hospitalisations.xml',
        'views/automated_actions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
