from odoo import fields,models

     
class AssuranceVie(models.Model):
    _name = 'assurfaz.vie'
    _description = 'Assurance Vie'
  

    name = fields.Char('Nom')
    state = fields.Selection([('nouvelle','Nouvelle'),
        ('validee','Validée'),
        ('acceptee','Acceptée'),
        ('refusee','Refusée')],
        default='nouvelle'
    )
    