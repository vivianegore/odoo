from odoo import fields, models

class Sinistre(models.Model):
    _name = 'assurfaz.sinistre'
    _description = 'Gestion de sinistre'
    

    
    name = fields.Char('Nom')
   

