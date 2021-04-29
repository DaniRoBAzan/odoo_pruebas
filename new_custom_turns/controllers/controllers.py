# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class TurnController(http.Controller):

    @http.route('/api/turns', auth='public', method=['GET'], csrf=False)
    def get_turns(self, **kw):
        try:
            visits = http.request.env['new_custom_turns.turn'].sudo().search_read([], ['id', 'name', 'customer', 'done'])
            res = json.dumps(visits, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

