# -*- coding: utf-8 -*-
{
    'name': "POS Receipt Credit info",

    'summary': "Credit information on Receipt",

    'description': """
        Added information of Credit of the customer to be printed on the POS Receipt
    """,

    'author': "Infosoft",
    'website': "https://www.infosoft.ae",

    'version': '17.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'custom_receipt/static/src/js/cus_receipt.js',
            'custom_receipt/static/src/xml/cus_receipt.xml',
            'custom_receipt/static/src/xml/total_receipt.xml',
        ]
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
}

