from email.policy import default
from odoo import fields, models


class ItqSkill(models.Model):
    _name = 'itq.skill'
    _description = 'Itq Skill'

    name = fields.Char(required=True)
    color = fields.Integer(required=True, default=0)
