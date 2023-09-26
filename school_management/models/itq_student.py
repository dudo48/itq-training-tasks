from datetime import datetime
from odoo import _, api, fields, models


class ItqStudent(models.Model):
    _name = 'itq.student'
    _description = 'Itq Student'

    name = fields.Char(required=True)
    course_id = fields.Many2one('itq.course', required=True)
    capacity = fields.Integer(related='course_id.capacity')
    join_date = fields.Date(required=True)
    birthday = fields.Date(required=True)
    age = fields.Integer(compute='_compute_age', required=True)
    skills_ids = fields.Many2many('itq.skill', required=True)

    @api.depends('birthday')
    def _compute_age(self):
        today = datetime.today()
        for record in self:
            if record.birthday:
                record.age = today.year - record.birthday.year
            else:
                record.age = 0
