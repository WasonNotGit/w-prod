# -*- coding: utf-8 -*-

from odoo import models, fields, api

class w_production_wason(models.Model):
    #_name = 'res.partner'
    _inherit = 'res.partner'
    is_promo = fields.Boolean (string = 'Промомодель')
    #, groups='base.group_user,base.group_system'
    # surname = fields.Char(string = "Фамилия")
    # name = fields.Char(string = "Имя")
    # fathername = fields.Char(string = "Отчество")
    #value = fields.Integer()
    #value2 = fields.Float(compute="_value_pc", store=True)
    #description = fields.Text()

    #@api.depends('value')
    #def _value_pc(self):
    #    self.value2 = float(self.value) / 100
 