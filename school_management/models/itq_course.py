from odoo import models, fields


class ItqCourse(models.Model):
    _name = 'itq.course'
    _description = 'itq.course'

    name = fields.Char(required=True)
    capacity = fields.Integer(required=True)
    instructor_id = fields.Many2one('itq.instructor', required=True)
