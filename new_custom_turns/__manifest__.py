# -*- coding: utf-8 -*-
{
    'name': "New Custom Turns",

    'summary': """
        new module created for handling custom shifts""",

    'description': """
        Module for custom shift...
    """,

    'author': "Romina Bazan",
    'website': "",
    'category': 'Uncategorized',
    'version': '14.0.0.1',
    'depends': ['base', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'reports/template_patient_turn_pdf.xml',
        'reports/report_action_patient_turn.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
