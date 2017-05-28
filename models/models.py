# -*- coding: utf-8 -*-

from odoo import models, fields, api

class w_production_girl_state_wason(models.Model):
    name = fields.Char ("Название статуса")
        

class w_production_wason(models.Model):
    #_name = 'res.partner'
    _inherit = 'res.partner'
    is_girl = fields.Boolean (string = 'W-модель', groups='w_production_wason.w_production_user')
    girl_birthdate = fields.Date (string = 'Дата рождения', groups='w_production_wason.w_production_user')
    girl_height = fields.Integer (string = 'Рост', groups='w_production_wason.w_production_user')
    girl_bust = fields.Integer (string = 'Обхват груди', groups='w_production_wason.w_production_user')
    girl_waist = fields.Integer (string = 'Обхват талии', groups='w_production_wason.w_production_user')
    girl_hips = fields.Integer (string = 'Обхват бёдер', groups='w_production_wason.w_production_user')
    girl_cups = fields.Selection ([(1,"1 размер (A)"),(2,"2 размер")],
        string = 'Размер бюста',
        groups='w_production_wason.w_production_user')
    girl_casting_date = fields.Datetime (string = 'Дата и время кастинга', groups='w_production_wason.w_production_user')
    girl_presentation_date = fields.Datetime (string = 'Дата и время презентации', groups='w_production_wason.w_production_user')
    girl_casting_done = fields.Boolean ("Кастинг проведён", groups='w_production_wason.w_production_user')
    girl_presentation_done = fields.Boolean ("Презентация проведена", groups='w_production_wason.w_production_user')
    girl_state_id = fields.Many2one('w_production_girl_state_wason', string='Текущий статус',
                               required=False, groups='w_production_wason.w_production_user')
    # stage_id = fields.Many2one(related='crm_lead_id.stage_id',
    #                                              readonly=True)

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
 