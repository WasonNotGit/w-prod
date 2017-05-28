# -*- coding: utf-8 -*-

from odoo import models, fields, api

class w_production_wason(models.Model):
    #_name = 'res.partner'
    _inherit = 'res.partner'
    is_model = fields.Boolean (string = 'Модель', groups='w_production_wason.w_production_user')
    model_birthdate = fields.Date (string = 'Дата рождения', groups='w_production_wason.w_production_user')
    model_height = fields.Integer (string = 'Рост', groups='w_production_wason.w_production_user')
    model_bust = fields.Integer (string = 'Обхват груди', groups='w_production_wason.w_production_user')
    model_waist = fields.Integer (string = 'Обхват талии', groups='w_production_wason.w_production_user')
    model_hips = fields.Integer (string = 'Обхват бёдер', groups='w_production_wason.w_production_user')
    model_cups = fields.Selection ([(1,"1 месяц"),(2,"2 месяца")],
        string = 'Размер бюста',
        groups='w_production_wason.w_production_user')
    model_casting_date = fields.Datetime (string = 'Дата и время кастинга', groups='w_production_wason.w_production_user')
    model_presentation_date = fields.Datetime (string = 'Дата и время презентации', groups='w_production_wason.w_production_user')
    model_casting_done = fields.Boolean ("Кастинг проведён", groups='w_production_wason.w_production_user')
    model_presentation_done = fields.Boolean ("Презентация проведена", groups='w_production_wason.w_production_user')
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
 