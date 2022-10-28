# -*- coding: utf-8 -*-

from email.policy import default
from symbol import factor
from odoo import models, fields, api

class NotaVenta(models.Model):
    _inherit = 'stock.picking'

    rma_id = fields.Many2one('repair.order',string='OTH')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        domain={'rma_id':[('partner_id','=',self.partner_id.id),('state','!=','done')]}
        return {'domain':domain}
