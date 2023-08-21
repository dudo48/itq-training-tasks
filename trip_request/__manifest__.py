# -*- coding: utf-8 -*-


{
    'name': "Trip Request",

    'summary': """
    """,

    'author': "Fady Emad",

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr',
        'hr_contract',
    ],

    # always loaded
    'data': [
        # Security files:
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',

        # Report files
        'reports/trip_request_report.xml',

        # Data files:

        # Root menu items files:

        # View files:
        'views/trip_request.xml',
        'views/employee.xml',

        # Menu items files:

    ],
}
