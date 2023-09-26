# -*- coding: utf-8 -*-


{
    'name': "School Management",

    'summary': """
    """,

    'author': "Fady Emad",

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base'
    ],

    # always loaded
    'data': [
        # Security files:
        'security/ir.model.access.csv',
        'security/groups.xml',
        'security/record_rules.xml',

        # Report files

        # Data files:

        # Root menu items files:

        # View files:
        'views/school_management.xml',
        'views/itq_student.xml',
        'views/itq_instructor.xml',
        'views/itq_course.xml',
        'views/itq_skill.xml',

        # Menu items files:

    ],
}
