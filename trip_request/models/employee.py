from odoo import models, fields


class Employee(models.Model):
    _inherit = 'hr.employee'

    allowed_destination_ids = fields.Many2many('res.country', string="Allowed Destinations")
    trip_request_id = fields.One2many('trip.request', 'employee_id', string="Trip Requests")
