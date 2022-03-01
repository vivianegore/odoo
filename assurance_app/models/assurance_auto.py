from odoo import fields, models

class AssuranceAuto(models.Model):
    _name = 'assurfaz.auto'
    _description = 'Assurance Auto'
   

    
    name = fields.Char('Nom')
    garantie_ids = fields.One2many('assurfaz.auto.garantie',"assurance_auto_id")
    vehicule_ids = fields.One2many('assurfaz.auto.vehicule',"assurance_auto_id")
