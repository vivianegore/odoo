from unittest import result
from odoo import fields,models,_ ,api
from odoo.exceptions import  UserError

     
class AssuranceSante(models.Model):
    _name = 'assurfaz.sante'
    _description = 'Assurance santé'
    _inherit = ['mail.thread']
  

    name = fields.Char('Nom')
    state = fields.Selection([('nouvelle','Nouvelle'),
        ('validee','Validée'),
        ('acceptee','Acceptée'),
        ('refusee','Refusée')],
        default='nouvelle'
    )

    montnt_total = fields.Float("Montant total de l'assurance en CFA")
    prime_id = fields.Many2one("assurfaz.prime")
    ref = fields.Char(default="Assurance Sante")

    
    def action_accepte(self):
        for rec in self:
            rec.state = 'acceptee'
            new_prime = self.env['assurfaz.prime'].create(
                    {
                        
                        'prime': (self.montnt_total * 10)/100,
                        'reference_prime': self.ref,
                        
                    }
                )
            rec.prime_id = new_prime.id
            return result
    

    def action_valide(self):
        for rec in self:
            rec.state = 'validee'

    def action_retour(self):
        for rec in self:
            rec.state = 'nouvelle'

    def action_refuse(self):
        for rec in self:
            rec.state = 'refusee' 
