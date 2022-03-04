from odoo import  fields, models

     
class ResPartner(models.Model):
    _inherit = 'res.partner'

    produit_assurance = fields.Selection([('auto','Assurance auto/moto'),('voyage','Assurance voyage'),
        ('habitation','Assurance habitation'),('sante','Assurance santé'),
        ('vie','Assurance vie')], 
        string ="Produits d'assurance",
        default='vie'
    )
    statut = fields.Selection([('nouveau','Nouveau '),('potentiel','Client potentiel'),
        ('important','Client important')],
        string ="Qualification du contact",
        default='potentiel'
    )


    
  
