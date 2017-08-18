from openerp import api, exceptions, fields, models


class StockTransferDetailsItems(models.Model):
    _inherit = 'stock.transfer_details_items'

    check_viscosity = fields.Boolean(
        related="product_id.product_tmpl_id.check_viscosity",
    )
    viscosity = fields.Float(
        digits=(6, 4),
    )

    @api.one
    @api.onchange('viscosity')
    def _get_product_oum_qty_viscosity(self):
        if self.viscosity > 0:
            self.quantity = self.quantity*self.viscosity
