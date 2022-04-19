from odoo import fields,models

     
class AssuranceVie(models.Model):
    _name = 'assurfaz.vie'
    _description = 'Assurance Vie'
    _inherit = ['mail.thread']
  

    name = fields.Char('Nom')
    state = fields.Selection([('nouvelle','Nouvelle'),
        ('validee','Validée'),
        ('acceptee','Acceptée'),
        ('refusee','Refusée')],
        default='nouvelle'
    )
    
    def action_valide(self):
        for rec in self:
            rec.state = 'validee'

    def action_retour(self):
        for rec in self:
            rec.state = 'nouvelle'

    def action_accepte(self):
        for rec in self:
            rec.state = 'acceptee'

    def action_refuse(self):
        for rec in self:
            rec.state = 'refusee' 
