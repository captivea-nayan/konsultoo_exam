{
    "name": "coupon management",
    "version": "1.0.0",
    "category": "",
    'summary': 'Coupon Management Data',
    'sequence': -100,
    "description": """customer coupon management data
   Description of the module. 
    """,
    "price": 000,
    "currency": 'EUR',
    "depends": ['base'],
    "data": ["security/ir.model.access.csv",
             # "report/coupon_generate_report.xml",
             # "report/coupon_generate_template_view.xml",
             "views/coupon_generator_view.xml",
             "views/coupon_master_ksc_view.xml",
             ],
    "auto_install": False,
    "installable": True,
    "application": True,
    "license": 'LGPL-3',
}
# -*- coding: utf-8 -*-
