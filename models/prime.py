from ast import Store
from unittest import result
from odoo import fields, models,api,_
import datetime

class Prime(models.Model):
    _name = 'assurfaz.prime'
    _description = 'Création de prime'
    _inherit = ['mail.thread']
    _rec_name = 'reference_prime'
    

    reference_prime = fields.Char("Référence de la prime ")
    date_creation = fields.Datetime("Date de création",default=fields.Datetime.now)
    prime = fields.Float("Prime d'assurance en CFA", compute='_get_prime_automatiquement', store="True")

    
   

   
   
   
   
   
   
   
   
   
   
