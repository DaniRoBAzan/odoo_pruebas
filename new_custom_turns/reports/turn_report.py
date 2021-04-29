# -*- coding: utf-8 -*-

from odoo import models, fields, api

#LA SIGUIENTE CLASE LA USAMOS PARA PODER IMPRIMIR EL PDF
class TurnReport(models.AbstractModel):
    _name='report.new_custom_turns.report_turn_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('new_custom_turns.report_turn_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['new_custom_turns.turn'],
            'docs': self.env['new_custom_turns.turn'].browse(docids)
        }
