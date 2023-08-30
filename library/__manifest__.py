# -*- coding: utf-8 -*-


{
    'name': "Library",

    'summary': """
    """,

    'author': "Fady Emad",

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        # Security files:
        'security/ir.model.access.csv',

        # Report files

        # Data files:
        'data/author_demo.xml',
        'data/book_demo.xml',

        # Root menu items files:

        # View files:
        'views/library.xml',
        'views/book.xml',
        'views/author.xml',
        'views/borrow_book_wizard.xml',

        # Menu items files:

    ],
}
