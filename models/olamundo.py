# -*- coding: utf-8 -*-

from odoo import models, fields, api


class olamundo(models.Model):
     _name = 'odoo_olamundo.olamundo'
     _description = 'Exemplo de ola mundo'

     name = fields.Char(string="Ola Mundo:")
     campo1 = fields.Text(string="Campo 1:")


