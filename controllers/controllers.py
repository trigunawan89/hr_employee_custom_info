# -*- coding: utf-8 -*-
# from odoo import http


# class HrEmployeeCustomInfo(http.Controller):
#     @http.route('/hr_employee_custom_info/hr_employee_custom_info/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_employee_custom_info/hr_employee_custom_info/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_employee_custom_info.listing', {
#             'root': '/hr_employee_custom_info/hr_employee_custom_info',
#             'objects': http.request.env['hr_employee_custom_info.hr_employee_custom_info'].search([]),
#         })

#     @http.route('/hr_employee_custom_info/hr_employee_custom_info/objects/<model("hr_employee_custom_info.hr_employee_custom_info"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_employee_custom_info.object', {
#             'object': obj
#         })
