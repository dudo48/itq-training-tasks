from odoo import models, fields, api


class BookBorrowWizard(models.TransientModel):
    _name = 'book.borrow.wizard'

    action = fields.Selection([('borrow', "Borrow"), ('return', "Return")], default='borrow')
    book_id = fields.Many2one('book', required=True)
    return_date = fields.Date()
    show_is_borrowed = fields.Boolean(compute='_compute_show_is_borrowed')

    @api.model
    def create(self, values):
        self.env['book'].browse(values['book_id']).write({
            'is_borrowed': values['action'] == 'borrow',
            'return_date': values.get('return_date', False),
        })
        return super(BookBorrowWizard, self).create(values)

    @api.depends('action')
    def _compute_show_is_borrowed(self):
        for record in self:
            record.show_is_borrowed = record.action == 'return'

    @api.onchange('action')
    def _reset_book_id(self):
        self.book_id = False
