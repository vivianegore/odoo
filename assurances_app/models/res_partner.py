from odoo import  fields, models

     
class ResPartner(models.Model):
    _inherit = 'res.partner'

    
    statut = fields.Selection([('nouveau','Nouveau '),('potentiel','Client potentiel'),
        ('important','Client important')],
        string ="Qualification du contact",
        default='potentiel'
    )
    produit_assurance_ids = fields.Many2many('assurfaz.typeassurance','typeassurance_partner_rel','partner_id','typeassurance_id')
    


    
  
