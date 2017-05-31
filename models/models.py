# -*- coding: utf-8 -*-

from odoo import models, fields, api

import datetime
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

class w_production_girl_state_wason(models.Model):
    name = fields.Char ("Название статуса")

def age_years(birthdate):
    born = datetime.datetime.strptime (birthdate, '%Y-%m-%d').date()
    today = datetime.datetime.today().date()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        

class w_production_wason(models.Model):
    #_name = 'res.partner'
    _inherit = 'res.partner'
    is_girl = fields.Boolean (string = 'W-модель')
    girl_birthdate = fields.Date (string = 'Дата рождения', groups='w_production_wason.w_production_user')
    girl_age = fields.Integer (string = 'Возраст', groups='w_production_wason.w_production_user')
    girl_height = fields.Integer (string = 'Рост', groups='w_production_wason.w_production_user')
    girl_bust = fields.Integer (string = 'Обхват груди', groups='w_production_wason.w_production_user')
    girl_waist = fields.Integer (string = 'Обхват талии', groups='w_production_wason.w_production_user')
    girl_hips = fields.Integer (string = 'Обхват бёдер', groups='w_production_wason.w_production_user')
    girl_casting_date = fields.Datetime (string = 'Дата и время кастинга', groups='w_production_wason.w_production_user')
    girl_presentation_date = fields.Datetime (string = 'Дата и время презентации', groups='w_production_wason.w_production_user')
    #girl_casting_done = fields.Boolean ("Кастинг проведён", groups='w_production_wason.w_production_user')
    #girl_presentation_done = fields.Boolean ("Презентация проведена", groups='w_production_wason.w_production_user')
    girl_state_id = fields.Many2one('w_production_girl_state_wason', string='Текущий статус',
                               required=False, groups='w_production_wason.w_production_user')
 
    @api.onchange ('girl_birthdate')    
    @api.multi
    def calculate_age(self):
        for rec in self:
            if rec.girl_birthdate:
                rec.girl_age = age_years (rec.girl_birthdate)

    @api.multi
    def write(self,vals):
        if vals.get('girl_birthdate'):
            vals['girl_age'] = age_years (vals['girl_birthdate'])
