# -*- coding: utf-8 -*-
{
    'name': "Check Print MX whit custom legend",

    'summary': """
        Formato de impresion de cheques para MX con leyenda personalizada por diario""",

    'description': """
    """,

    'author': "Xmarts",
    'website': "https://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_check_printing','account_check_printing_report_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
