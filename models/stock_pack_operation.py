from odoo import api, exceptions, fields, models


class StopckPackOperation(models.Model):
    _inherit = 'stock.pack.operation'

    check_viscosity = fields.Boolean(
        related="product_id.product_tmpl_id.check_viscosity",
    )
    viscosity = fields.Float(
        digits=(6, 4),
    )
    kg = fields.Float(
        digits=(6, 4),
    )

    @api.multi
    @api.onchange('viscosity', 'kg')
    def _get_product_oum_qty_viscosity(self):
        for r in self:
            if r.viscosity > 0:
                r.product_qty = r.viscosity*r.kg
