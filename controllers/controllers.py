# API Connector
# XMLRPC Style for Odoo
# Main Dev: Ignacio Buioli <ibuioli@gmail.com>
# Codize - https://www.codize.ar

# -*- coding: utf-8 -*-
import logging

import odoo
from odoo import http
from odoo.http import request
import re
import xmlrpc.client

_logger = logging.getLogger(__name__)
CORS = '*'

ALLOWED_METHODS = {
    'stock.picking': ['button_validate', 'action_done'],
    'sale.order': ['action_confirm'],
}

class OdooApiXMLRPC(http.Controller):
    # version #
    @http.route('/odoo-api/common/version', type="json", auth='none', cors=CORS)
    def odoo_api_version(self, **kw):
        common = xmlrpc.client.ServerProxy('http://127.0.0.1:8069/xmlrpc/2/common')
        return common.version()

    # login #
    @http.route('/odoo-api/common/login', type="json", auth='none', cors=CORS)
    def odoo_api_login(self, db=None, login=None, password=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            return {
                "user_uid": uid,
                "authentification": True
            }
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # fields_get #
    @http.route('/odoo-api/object/fields_get', type="json", auth='none', cors=CORS)
    def odoo_api_fields_get(self, model, db=None, login=None, password=None, keys={}, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                attributes = None
                allfields = None
                if 'attributes' in keys.keys():
                    attributes = keys['attributes']
                if 'allfields' in keys.keys():
                    allfields = keys['allfields']

                return request.env[model].browse(uid).fields_get(attributes=attributes, allfields=allfields)
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # search_count #
    @http.route('/odoo-api/object/search_count', type="json", auth='none', cors=CORS)
    def odoo_api_search_count(self, model, filters=None, db=None, login=None, password=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                return request.env[model].browse(uid).search_count(filters)
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # search #
    @http.route('/odoo-api/object/search', type="json", auth='none', cors=CORS)
    def odoo_api_search(self, model, filters=None, keys={}, db=None, login=None, password=None, attributes=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                limit = None
                offset = None
                order = None
                count = False
                context={}

                if 'limit' in keys.keys():
                    limit = keys['limit']
                if 'offset' in keys.keys():
                    offset = keys['offset']
                if 'order' in keys.keys():
                    order = keys['order']
                if 'count' in keys.keys():
                    count = keys['count']
                if 'context' in keys.keys():
                    context=keys['context']

                ans = []
                model = request.env[model].browse(uid).with_context(context).search(filters, limit=limit, offset=offset, order=order, count=count)
                for m in model:
                    ans.append(m.id)
                return ans
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # read #
    @http.route('/odoo-api/object/read', type="json", auth='none', cors=CORS)
    def odoo_api_read(self, model, ids=None, keys={}, db=None, login=None, password=None, attributes=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                fields = None

                if 'fields' in keys.keys():
                    fields = keys['fields']

                model = request.env[model].browse(uid).browse(ids).read(fields=fields)
                return model
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # search_read #
    @http.route('/odoo-api/object/search_read', type="json", auth='none', cors=CORS)
    def odoo_api_search_read(self, model, filters=None, keys={}, db=None, login=None, password=None, attributes=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                limit = None
                offset = 0
                order = None
                fields = None
                context={}

                if 'limit' in keys.keys():
                    limit = keys['limit']
                if 'offset' in keys.keys():
                    offset = keys['offset']
                if 'order' in keys.keys():
                    order = keys['order']
                if 'fields' in keys.keys():
                    fields = keys['fields']
                if 'context' in keys.keys():
                    context=keys['context']

                model = request.env[model].browse(uid).with_context(context).search_read(filters, limit=limit, offset=offset, order=order, fields=fields)
                return model
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # write #
    @http.route('/odoo-api/object/write', type="json", auth='none', cors=CORS)
    def odoo_api_write(self, model, id=None, vals={}, db=None, login=None, password=None, attributes=None, **kw):
        """
          Doc for One2many & Many2many
          ``(0, 0, values)``
              adds a new record created from the provided ``value`` dict.
          ``(1, id, values)``
              updates an existing record of id ``id`` with the values in
              ``values``. Can not be used in :meth:`~.create`.
          ``(2, id, 0)``
              removes the record of id ``id`` from the set, then deletes it
              (from the database). Can not be used in :meth:`~.create`.
          ``(3, id, 0)``
              removes the record of id ``id`` from the set, but does not
              delete it. Can not be used in
              :meth:`~.create`.
          ``(4, id, 0)``
              adds an existing record of id ``id`` to the set.
          ``(5, 0, 0)``
              removes all records from the set, equivalent to using the
              command ``3`` on every record explicitly. Can not be used in
              :meth:`~.create`.
          ``(6, 0, ids)``
              replaces all existing records in the set by the ``ids`` list,
              equivalent to using the command ``5`` followed by a command
              ``4`` for each ``id`` in ``ids``.
        """
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                model = request.env[model].browse(uid).browse(id).write(vals)
                return model
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # create #
    @http.route('/odoo-api/object/create', type="json", auth='none', cors=CORS)
    def odoo_api_create(self, model, vals={}, db=None, login=None, password=None, attributes=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                model = request.env[model].browse(uid).create(vals)
                return model.id
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # unlink #
    @http.route('/odoo-api/object/unlink', type="json", auth='none', cors=CORS)
    def odoo_api_unlink(self, model, id=None, db=None, login=None, password=None, attributes=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                model = request.env[model].browse(uid).browse(id).unlink()
                return model
        except Exception as e:
            return {'status': False, 'error': str(e)}
        
    # report #
    @http.route('/odoo-api/object/report', type="json", auth='none', cors=CORS)
    def odoo_api_report(self, model, id=None, report_name=None, db=None, login=None, password=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                import base64
                #model = request.env[model].browse(uid).ref(report_name).render_qweb_pdf([id])[0]    # ver. 11, 12, 13
                model = request.env[model].browse(uid).ref(report_name)._render_qweb_pdf([id])[0]    # ver. 14+
                pdf = base64.b64encode(model)
                return pdf
        except Exception as e:
            return {'status': False, 'error': str(e)}
        
    # execute_method (genérico) #
    @http.route('/odoo-api/object/execute_method', type="json", auth='none', cors=CORS)
    def odoo_api_execute_method(self, model, ids, method, args=[], kwargs={}, db=None, login=None, password=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                # Validar whitelist
                allowed = ALLOWED_METHODS.get(model, [])
                if method not in allowed:
                    return {'status': False, 'error': f"Método '{method}' no permitido para {model}"}

                records = request.env[model].sudo().browse(ids)
                fn = getattr(records, method, None)

                if fn and callable(fn):
                    result = fn(*args, **kwargs)
                    _logger.info(f"Executed {model}.{method} with args={args} kwargs={kwargs} result={result}")
                    if hasattr(result, 'ids'):
                        return {'status': True, 'method': method, 'model': model, 'ids': result.ids}
                    elif isinstance(result, (dict, list, str, int, float, bool)):
                        return {'status': True, 'method': method, 'model': model, 'result': result}
                    else:
                        return {'status': True, 'method': method, 'model': model, 'result': str(result)}
                else:
                    return {'status': False, 'error': f"Método '{method}' no encontrado en {model}"}
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # action #
    # Model for action request, adapt for your need
    #@http.route('/odoo-api/object/action', type="json", auth='none', cors=CORS)
    #def odoo_api_action(self, model, id=None, action=None, vals={}, db=None, login=None, password=None, attributes=None, **kw):
    #    try:
    #        uid = request.session.authenticate(db, login, password)
    #        if uid:
    #            if action == "action_create_payments" and model == "account.move":
    #                payment_register = request.env['account.payment.register'].browse(uid)
    #                _action = payment_register.with_context(
    #                    {'active_model': 'account.move',
    #                     'active_ids': id}
    #                ).create({}).action_create_payments()
    #            else :
    #                model = request.env[model].browse(uid).browse(id)
    #                _action = getattr(model, action)(**vals)
    #            return {
    #                "model": model,
    #                "action": action,
    #                "return": _action
    #            }
    #    except Exception as e:
    #        return {'status': False, 'error': str(e)}
