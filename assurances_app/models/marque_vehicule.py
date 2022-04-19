from odoo import fields, models

class Marque(models.Model):
    _name = 'assurfaz.auto.vehicule.marque'
    _description = 'Marques véhicules'
    _inherit = ['mail.thread']

    name = fields.Char(string="Marque")
    #marque = fields.Char()
    
    