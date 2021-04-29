# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class Turn(models.Model):
    _name = 'new_custom_turns.turn'
    _description = 'Turn'

    customer = fields.Many2one(string='Patient', comodel_name='res.partner')
    name = fields.Char(string='Description')
    date = fields.Datetime(string='Date')
    type = fields.Selection([('P', 'Face-to-face'), ('W', 'WhatsApp'), ('T', 'Telephone')], string='Type', required=True)
    done = fields.Boolean(string='Attended', readonly=True)
    image = fields.Binary(string='Image')

    # FUNCION DE BOTON
    def toggle_state(self):
        self.done = not self.done

    def f_duplicate(self):
        turn = {
            'name': 'Double turn',
            'customer': self.customer.id,
            'date': fields.Date.today(),
            'type': 'P',
            'done': False
        }
        self.env['new_custom_turns.turn'].create(turn)

    def f_change_done(self):
        if self.done == True:
            self.done = False
        else:
            self.done = True

    def f_delete(self):
        turn = self.env['new_custom_turns.turn'].search([('id','=',self.id)])
        turn.unlink()


# #LA SIGUIENTE CLASE LA USAMOS PARA PODER IMPRIMIR EL PDF
# class TurnReport(models.AbstractModel):
#     _name='report.new_custom_turns.report_turn_card'
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         report_obj = self.env['ir.actions.report']
#         report = report_obj._get_report_from_name('new_custom_turns.report_turn_card')
#         return {
#             'doc_ids': docids,
#             'doc_model': self.env['new_custom_turns.turn'],
#             'docs': self.env['new_custom_turns.turn'].browse(docids)
#         }


class CustomSaleOrder(models.Model):

    _inherit = 'sale.order'

    zone = fields.Selection([('N', 'North'), ('C', 'Center'), ('S', 'South')], string='Zone')