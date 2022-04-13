from odoo import fields, models

class Prime(models.Model):
    _name = 'assurfaz.prime'
    _description = 'Gestion de prime'
    _inherit = ['mail.thread']
    

    
    name = fields.Char('Nom')
   

