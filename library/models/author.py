from odoo import models, fields


class Author(models.Model):
    _name = 'author'

    name = fields.Char()
    book_ids = fields.One2many('book', inverse_name='author_id', string="Books")
