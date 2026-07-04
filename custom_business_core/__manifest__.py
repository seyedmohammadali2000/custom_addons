# -*- coding: utf-8 -*-
{
    'name': 'Custom Business Core',
    'version': '1.0.2',
    'category': 'Sales',
    'summary': 'Core business extension for enterprise workflow',
    'description': """
Core Business Customization
==========================
Internal module for structural business logic extensions.
""",
    'author': 'Almahdi',
    'depends': ['base', 'sale', 'stock'],
    'data': [
        'views/business_task_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}