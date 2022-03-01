from odoo import fields,models

     
class AssuranceSante(models.Model):
    _name = 'assurfaz.sante'
    _description = 'Assurance santé'
  

    name = fields.Char('Nom')