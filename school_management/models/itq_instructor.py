from odoo import models, fields


class ItqInstructor(models.Model):
    _name = 'itq.instructor'
    _description = 'itq.instructor'

    name = fields.Char(related='partner_id.name')
    partner_id = fields.Many2one('res.partner', required=True)
    course_ids = fields.One2many('itq.course', 'instructor_id', required=True)
