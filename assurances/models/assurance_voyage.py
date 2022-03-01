from odoo import fields,models

     
class AssuranceVoyage(models.Model):
    _name = 'assurfaz.voyage'
    _description = 'Assurance Voyage'
  

    name = fields.Char('Nom')