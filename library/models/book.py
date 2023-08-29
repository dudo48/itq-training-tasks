from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'book'

    name = fields.Char(required=True)
    author_id = fields.Many2one('author', required=True)
    publication_date = fields.Date(required=True)
    isbn = fields.Char(required=True, string="ISBN")
    is_borrowed = fields.Boolean(required=True, string="Borrowed?")
    return_date = fields.Date()

    def borrow_book(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False
        self.return_date = False
