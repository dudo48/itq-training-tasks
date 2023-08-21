from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _name = 'trip.request'

    employee_id = fields.Many2one('hr.employee', required=True, domain=[('contract_id.state', '=', 'open')])
    destination_id = fields.Many2one('res.country', required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    trip_days = fields.Integer(compute='_compute_trip_days')
    rest_days = fields.Integer(required=True)
    status = fields.Selection(
        [
            ('draft', "Draft"),
            ('confirmed', "Confirmed"),
            ('ended', "Ended"),
            ('cancelled', "Cancelled")
        ],
        required=True
    )
    last_changed_status_by_id = fields.Many2one('res.users')

    @api.depends('start_date', 'end_date')
    def _compute_trip_days(self):
        for record in self:
            if record.start_date and record.end_date:
                record.trip_days = (record.end_date - record.start_date).days + 1
            else:
                record.trip_days = 0

    @api.onchange('employee_id')
    def _get_destination_domain(self):
        return {
            'domain': {
                'destination_id': [('id', 'in', self.employee_id.allowed_destination_ids.mapped('id'))]
            }
        }

    @api.onchange('status')
    def _onchange_status(self):
        self.last_changed_status_by_id = self.env.user

    @api.onchange('start_date')
    def _empty_end_date(self):
        if self.start_date:
            self.end_date = False

    @api.constrains('start_date', 'end_date')
    def _check_date_constraint(self):
        for record in self:
            if record.start_date > record.end_date:
                raise ValidationError("Start date cannot be later than end date")

    @api.constrains('rest_days')
    def _check_rest_days_constraint(self):
        for record in self:
            if record.rest_days < 0:
                raise ValidationError("Rest days cannot be less than 0")