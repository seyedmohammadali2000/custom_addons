# -*- coding: utf-8 -*-

from odoo import models, fields


class BusinessTask(models.Model):
    _name = 'business.task'
    _description = 'Business Operational Task'

    name = fields.Char(string='Task Title', required=True)
    description = fields.Text(string='Description')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High')
    ], string='Priority', default='1')
    kanban_state = fields.Selection([
        ('normal', 'In Progress'),
        ('done', 'Ready'),
        ('blocked', 'Blocked')
    ], string='Status', default='normal')
    date_deadline = fields.Date(string='Deadline')