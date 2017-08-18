from openerp import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    kilograms = fields.Float(
        compute='_get_kilograms',
        digits=(10, 3),
    )

    @api.one
    @api.depends('product_id', 'product_qty')
    def _get_kilograms(self):
        self.kilograms = -1
        if self.product_id.viscosity != 0:
            self.kilograms = self.product_qty/self.product_id.viscosity
