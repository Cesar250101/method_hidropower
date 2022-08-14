# -*- coding: utf-8 -*-
from odoo import http

# class MethodHidropower(http.Controller):
#     @http.route('/method_hidropower/method_hidropower/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_hidropower/method_hidropower/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_hidropower.listing', {
#             'root': '/method_hidropower/method_hidropower',
#             'objects': http.request.env['method_hidropower.method_hidropower'].search([]),
#         })

#     @http.route('/method_hidropower/method_hidropower/objects/<model("method_hidropower.method_hidropower"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_hidropower.object', {
#             'object': obj
#         })