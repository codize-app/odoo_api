# API Connector
# XMLRPC Style for Odoo
# Main Dev: Ignacio Buioli <ibuioli@gmail.com> or <ignacio.buioli@moldeointeractive.com.ar>
# Moldeo Interactive - https://www.moldeointeractive.com.ar

# -*- coding: utf-8 -*-
import odoo
from odoo import http
from odoo.http import request
import re

class OdooApiXMLRPC(http.Controller):
    @http.route('/odoo-api/common/version', type="json", auth='none', cors='*')
    def odoo_api_version(self, **kw):
        version = odoo.release.version.split('.')
        return {
            "server_version": version[0] + "." + version[1],
            "server_version_info": [int(version[0]), int(version[1]), 0, "final", 0],
            "server_serie": version[0] + "." + version[1],
            "protocol_version": 1,
        }

    @http.route('/odoo-api/common/login', type="json", auth='none', cors='*')
    def odoo_api_login(self, db=None, login=None, password=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            return uid
        except:
            return {'status': False}

    @http.route('/odoo-api/object/fields_get', type="json", auth='none', cors='*')
    def odoo_api_fields_get(self, model, db=None, login=None, password=None, keys=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                attributes=None
                allfields=None
                if 'attributes' in keys.keys():
                    attributes=keys['attributes']
                if 'allfields' in keys.keys():
                    allfields=keys['allfields']

                return request.env[model].browse(uid).fields_get(attributes=attributes, allfields=allfields)
            else:
                return {'status': False, 'error': 'Authorization err'}
        except:
            return {'status': False}

    @http.route('/odoo-api/object/search_count', type="json", auth='none', cors='*')
    def odoo_api_search_count(self, model, filters=None, db=None, login=None, password=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                return request.env[model].browse(uid).search_count(filters)
            else:
                return {'status': False, 'error': 'Authorization err'}
        except:
            return {'status': False}

    @http.route('/odoo-api/object/search', type="json", auth='none', cors='*')
    def odoo_api_search(self, model, filters=None, keys={}, db=None, login=None, password=None, attributes=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                limit=None
                offset=None
                order=None
                count=False

                if 'limit' in keys.keys():
                    limit=keys['limit']
                if 'offset' in keys.keys():
                    offset=keys['offset']
                if 'order' in keys.keys():
                    order=keys['order']
                if 'count' in keys.keys():
                    count=keys['count']

                ans = []
                model = request.env[model].browse(uid).search(filters, limit=limit, offset=offset, order=order, count=count)
                for m in model:
                    ans.append(m.id)
                return ans
            else:
                return {'status': False, 'error': 'Authorization err'}
        except:
            return {'status': False}

    @http.route('/odoo-api/object/read', type="json", auth='none', cors='*')
    def odoo_api_read(self, model, ids=None, keys={}, db=None, login=None, password=None, attributes=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                fields=None

                if 'fields' in keys.keys():
                    fields=keys['fields']

                model = request.env[model].browse(uid).browse(ids).read(fields=fields)
                return model
            else:
                return {'status': False, 'error': 'Authorization err'}
        except:
            return {'status': False}

    @http.route('/odoo-api/object/search_read', type="json", auth='none', cors='*')
    def odoo_api_search_read(self, model, filters=None, keys={}, db=None, login=None, password=None, attributes=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                limit=None
                offset=0
                order=None
                fields=None

                if 'limit' in keys.keys():
                    limit=keys['limit']
                if 'offset' in keys.keys():
                    offset=keys['offset']
                if 'order' in keys.keys():
                    order=keys['order']
                if 'fields' in keys.keys():
                    fields=keys['fields']

                model = request.env[model].browse(uid).search_read(filters, limit=limit, offset=offset, order=order, fields=fields)
                return model
            else:
                return {'status': False, 'error': 'Authorization err'}
        except:
            return {'status': False}

    @http.route('/odoo-api/object/write', type="json", auth='none', cors='*')
    def odoo_api_write(self, model, id=None, vals={}, db=None, login=None, password=None, attributes=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                model = request.env[model].browse(uid).browse(id).write(vals)
                return model
            else:
                return {'status': False, 'error': 'Authorization err'}
        except:
            return {'status': False}