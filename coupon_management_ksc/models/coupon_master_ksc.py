from odoo import models, fields
from datetime import datetime
import random, string


class CouponMasterKsc(models.Model):
    _name = 'coupon.master.ksc'

    def get_default_currency(self):
        return self.env.company.currency_id.id

    name = fields.Char(string='Name', size=8)
    start_date = fields.Date(string='Start Date', default=datetime.today())
    end_date = fields.Date(string='End Date', default=datetime.today())
    coupon_value = fields.Monetary(currency_field='currency_id', string="Coupon Value")
    currency_id = fields.Many2one('res.currency', default=get_default_currency)
    generator_id = fields.Many2one('coupon.generator.ksc')

    _sql_constraints = [

        ('unique_name', 'unique(name)', 'The master name  must be unique  !')

    ]

    def randomword(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
