from odoo import fields, models

class Assurance(models.Model):
    _name = 'assurance.assurfaz'
    _description = 'Assurance'
    _order = "name"

    
    name = fields.Char('Nom')
   

