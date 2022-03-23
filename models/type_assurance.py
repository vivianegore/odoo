from odoo import  fields, models

     
class TypeAssurance(models.Model):
    _name = 'assurfaz.typeassurance'
    _description = "Type d'assurances"
    _rec_name = 'type_assurance'
    
    type_assurance = fields.Selection([('Assurance auto/moto','auto'),('Assurance voyage','voyage'),
    ('Assurance habitation','habitation'),('Assurance santé','sante'),
    ('Assurance vie','vie')], 
        string ="Produits d'assurance"
    )  
   