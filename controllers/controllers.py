# API Connector
# XMLRPC Style for Odoo
# Main Dev: Ignacio Buioli <ibuioli@gmail.com> or <ignacio.buioli@moldeointeractive.com.ar>
# Moldeo Interactive - https://www.moldeointeractive.com.ar

# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import re

class OdooApiXMLRPC(http.Controller):
    @http.route('/odoo-api/common/version', type="json", auth='none', cors='*')
    def odoo_api_version(self, **kw):
        model = request.env['ir.module.module'].sudo().search([('name', '=', 'base')], limit=1)
        version = model.installed_version.split('.')
        return {
            "server_version": version[0] + ".0",
            "server_version_info": [int(version[0]), 0, 0, "final", 0],
            "server_serie": version[0] + ".0",
            "protocol_version": 1,
        }

    @http.route('/odoo-api/common/login', type="json", auth='none', cors='*')
    def odoo_api_login(self, **kw):
        try:
            uid = request.session.authenticate(kw['db'], kw['login'], kw['password'])
            return uid
        except:
            return {'status': False}

    @http.route('/odoo-api/object/fields_get', type="json", auth='none', cors='*')
    def odoo_api_fields_get(self, model, db=None, login=None, password=None, attributes=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                return request.env[model].browse(uid).fields_get(attributes=attributes)
            else:
                return {'status': False, 'error': 'Authorization err'}
        except:
            return {'status': False}