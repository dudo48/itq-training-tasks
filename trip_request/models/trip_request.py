from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _name = 'trip.request'

    employee_id = fields.Many2one('hr.employee', required=True, domain=[('contract_id.state', '=', 'open')])
    destination_id = fields.Many2one('res.country', required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    trip_days = fields.Integer(compute='_compute_trip_days', store=True)
    rest_days = fields.Integer(required=True)
    state = fields.Selection(
        [
            ('draft', "Draft"),
            ('confirmed', "Confirmed"),
            ('ended', "Ended"),
            ('cancelled', "Cancelled")
        ],
        required=True,
        default='draft'
    )
    last_changed_state_by_id = fields.Many2one('res.users', readonly=True)
    allowed_destination_ids = fields.Many2many(related='employee_id.allowed_destination_ids')

    def write(self, vals):
        if 'state' in vals:
            vals['last_changed_state_by_id'] = self.env.user
        return super(Employee, self).write(vals)

    @api.depends('start_date', 'end_date', 'rest_days')
    def _compute_trip_days(self):
        for record in self:
            if record.start_date and record.end_date:
                record.trip_days = (record.end_date - record.start_date).days - record.rest_days + 1
            else:
                record.trip_days = 0

    # @api.onchange('employee_id')
    # def _get_destination_domain(self):
    #     return {
    #         'domain': {
    #             'destination_id': [('id', 'in', self.employee_id.allowed_destination_ids.mapped('id'))]
    #         }
    #     }

    @api.onchange('start_date')
    def _empty_end_date(self):
        if self.start_date:
            self.end_date = False

    @api.constrains('start_date', 'end_date')
    def _check_date_constraint(self):
        for record in self:
            if record.start_date > record.end_date:
                raise ValidationError("Start date cannot be later than end date")

    @api.constrains('destination_id')
    def _check_destination_id_constraint(self):
        for record in self:
            if record.destination_id.id not in record.employee_id.allowed_destination_ids.mapped('id'):
                raise ValidationError("Destination can not be outside the allowed destinations list for the employee")

    @api.constrains('rest_days')
    def _check_rest_days_constraint(self):
        for record in self:
            if record.rest_days < 0:
                raise ValidationError("Rest days cannot be less than 0")
            if record.rest_days > (record.end_date - record.start_date).days + 1:
                raise ValidationError("Rest days cannot be greater than total trip request days")
