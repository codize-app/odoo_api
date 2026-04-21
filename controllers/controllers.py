# API Connector
# XMLRPC Style for Odoo with AUTH
# Main Devs:
# - Ignacio Buioli
# - Martin Bruno
# Codize - https://www.codize.ar

# -*- coding: utf-8 -*-
import logging

import odoo
from odoo import http
from odoo.http import request
import re
import hmac as _hmac
import hashlib
import time
import os
import xmlrpc.client

_logger = logging.getLogger(__name__)
CORS = '*'
ALLOWED_METHODS = []
_signing_key = None

# ─── HMAC helpers ─────────────────────────────────────────────────────────────

def _get_key():
    global _signing_key
    if _signing_key:
        return _signing_key
    path = os.path.join(odoo.tools.config['data_dir'], 'api_key.bin')
    if os.path.exists(path):
        with open(path, 'rb') as f:
            _signing_key = f.read()
    else:
        _signing_key = os.urandom(32)
        with open(path, 'wb') as f:
            f.write(_signing_key)
    return _signing_key

def _make_token(uid):
    exp = int(time.time()) + 86400 * 7  # 7 días
    payload = f"{uid}:{exp}"
    sig = _hmac.new(_get_key(), payload.encode(), hashlib.sha256).hexdigest()
    return f"{payload}:{sig}"

def _verify_token(token):
    if not token:
        return None
    try:
        i = token.rfind(':')
        sig = token[i + 1:]
        payload = token[:i]
        expected = _hmac.new(_get_key(), payload.encode(), hashlib.sha256).hexdigest()
        if not _hmac.compare_digest(sig, expected):
            return None
        uid_s, exp_s = payload.split(':', 1)
        if int(exp_s) < int(time.time()):
            return None
        return int(uid_s)
    except Exception:
        return None

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
            if not uid:
                return {'status': False, 'error': 'AUTH_REQUIRED'}
            return {'uid': uid, 'token': _make_token(uid)}
        except Exception as e:
            return {'status': False, 'error': str(e)}

    def _env(self, uid):
        return request.env(user=uid, su=True)

    # fields_get #
    @http.route('/odoo-api/object/fields_get', type="json", auth='none', cors=CORS)
    def odoo_api_fields_get(self, model, keys={}, token=None, **kw):
        uid = _verify_token(token)
        if not uid:
            return {'error': 'TOKEN_INVALID'}
        try:
            attributes = keys.get('attributes')
            allfields = keys.get('allfields')
            return self._env(uid)[model].fields_get(attributes=attributes, allfields=allfields)
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # search_count #
    @http.route('/odoo-api/object/search_count', type="json", auth='none', cors=CORS)
    def odoo_api_search_count(self, model, filters=None, token=None, **kw):
        uid = _verify_token(token)
        if not uid:
            return {'error': 'TOKEN_INVALID'}
        try:
            return self._env(uid)[model].search_count(filters)
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # search #
    @http.route('/odoo-api/object/search', type="json", auth='none', cors=CORS)
    def odoo_api_search(self, model, filters=None, keys={}, token=None, **kw):
        uid = _verify_token(token)
        if not uid:
            return {'error': 'TOKEN_INVALID'}
        try:
            limit = keys.get('limit')
            offset = keys.get('offset')
            order = keys.get('order')
            count = keys.get('count', False)
            records = self._env(uid)[model].search(filters, limit=limit, offset=offset, order=order, count=count)
            return [m.id for m in records]
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # read #
    @http.route('/odoo-api/object/read', type="json", auth='none', cors=CORS)
    def odoo_api_read(self, model, ids=None, keys={}, token=None, **kw):
        uid = _verify_token(token)
        if not uid:
            return {'error': 'TOKEN_INVALID'}
        try:
            fields = keys.get('fields')
            return self._env(uid)[model].browse(ids).read(fields=fields)
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # search_read #
    @http.route('/odoo-api/object/search_read', type="json", auth='none', cors=CORS)
    def odoo_api_search_read(self, model, filters=None, keys={}, token=None, **kw):
        uid = _verify_token(token)
        if not uid:
            return {'error': 'TOKEN_INVALID'}
        try:
            limit = keys.get('limit')
            offset = keys.get('offset', 0)
            order = keys.get('order')
            fields = keys.get('fields')
            return self._env(uid)[model].search_read(filters, limit=limit, offset=offset, order=order, fields=fields)
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # write #
    @http.route('/odoo-api/object/write', type="json", auth='none', cors=CORS)
    def odoo_api_write(self, model, id=None, vals={}, token=None, **kw):
        uid = _verify_token(token)
        if not uid:
            return {'error': 'TOKEN_INVALID'}
        try:
            return self._env(uid)[model].browse(id).write(vals)
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # create #
    @http.route('/odoo-api/object/create', type="json", auth='none', cors=CORS)
    def odoo_api_create(self, model, vals={}, token=None, **kw):
        uid = _verify_token(token)
        if not uid:
            return {'error': 'TOKEN_INVALID'}
        try:
            return self._env(uid)[model].create(vals).id
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # unlink #
    @http.route('/odoo-api/object/unlink', type="json", auth='none', cors=CORS)
    def odoo_api_unlink(self, model, id=None, token=None, **kw):
        uid = _verify_token(token)
        if not uid:
            return {'error': 'TOKEN_INVALID'}
        try:
            return self._env(uid)[model].browse(id).unlink()
        except Exception as e:
            return {'status': False, 'error': str(e)}

    # execute_method #
    @http.route('/odoo-api/object/execute_method', type="json", auth='none', cors=CORS)
    def odoo_api_execute_method(self, model, ids, method, args=[], kwargs={}, token=None, **kw):
        uid = _verify_token(token)
        if not uid:
            return {'error': 'TOKEN_INVALID'}
        try:
            allowed = ALLOWED_METHODS.get(model, [])
            if method not in allowed:
                return {'status': False, 'error': f"Método '{method}' no permitido para {model}"}
            records = self._env(uid)[model].browse(ids)
            fn = getattr(records, method, None)
            if fn and callable(fn):
                result = fn(*args, **kwargs)
                _logger.info("Executed %s.%s", model, method)
                if hasattr(result, 'ids'):
                    return {'status': True, 'method': method, 'model': model, 'ids': result.ids}
                elif isinstance(result, (dict, list, str, int, float, bool)):
                    return {'status': True, 'method': method, 'model': model, 'result': result}
                else:
                    return {'status': True, 'method': method, 'model': model, 'result': str(result)}
            return {'status': False, 'error': f"Método '{method}' no encontrado en {model}"}
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
