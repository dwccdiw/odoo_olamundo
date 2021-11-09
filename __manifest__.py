# -*- coding: utf-8 -*-
{
    'name': "odoo_olamundo",

    'summary': """
        Proxecto Inicial ola_mundo""",

    'description': """
        Proxecto Inicial ola_mundo, proxecto para iniciarnos en odoo
    """,

    'author': "Antonio",
    'website': "http://www.edu.xunta.gal/centros/iesteis",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/olamundo.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
