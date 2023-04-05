from odoo import models, fields, api
from datetime import datetime


class CouponGeneratorKsc(models.Model):
    _name = 'coupon.generator.ksc'

    def get_default_currency(self):
        return self.env.company.currency_id.id

    name = fields.Char(string="Name")
    number_of_coupon = fields.Integer()
    start_date = fields.Date(string="Start Date", default=datetime.today())
    end_date = fields.Date(string="End Date", default=datetime.today())
    customer_ids = fields.Many2many('res.partner', string="Customer Id")
    coupons_ids = fields.One2many(comodel_name='coupon.master.ksc', inverse_name='generator_id',
                                  string='Coupon Lines')
    total_value = fields.Monetary(currency_field='currency_id', string='Total Value', compute="_compute_total_value")
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  default=get_default_currency)

    # def generate_coupon_lines(self):
    #

    def generate_coupon_lines(self):
        self.coupons_ids = [(0, 0, {
            'name': self.name,
            'start_date': self.start_date,
            'end_date': self.start_date,
            'coupon_value': self.coupon_value,
            'generator_id': self.generator_id,
            'currency_id': self.currency_id,
        })]

    # invoice = self.env[‘account.move
    # '].create({
    # 'move_type': 'out_invoice',
    # 'invoice_date': datetime.now(),
    # 'invoice_line_ids': (0, 0, {
    #     'product_id': self.product_id,
    #     'price_unit': self.price_unit,
    # })],
    # })

    @api.model
    def create(self, vals):
        res = super(CouponGeneratorKsc, self).create(vals)
        print("---------------helooo", res)
        return res

    def _compute_total_value(self):
        for rec in self:
            rec.total_value = sum(rec.coupons_ids.mapped('coupon_value'))
