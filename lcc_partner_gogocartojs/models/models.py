from odoo import models, fields, api

# class lcc_partner_gogocartojs(models.Model):
#     _name = 'partner_gogocartojs.lcc_partner_gogocartojs'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100