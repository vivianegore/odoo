from odoo import fields,models

     
class AssuranceVie(models.Model):
    _name = 'assurfaz.vie'
    _description = 'Assurance Vie'
  

    name = fields.Char('Nom')
    demande_type= fields.Selection([('vousmeme','Vous faites une demande pour vous même en tant que bénéficiaire et éventuellement pour d\'autres personnes'),
        ('tiers','Vous faites une demande pour le compte d\'un tiers bénéficiaire')],
        string= 'Quelle est votre demande? ',
        default='tiers'
    )
    