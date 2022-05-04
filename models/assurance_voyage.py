from unittest import result
from odoo import fields,models,api,_
from dateutil.relativedelta import *
import datetime
from odoo.exceptions import  UserError
     
class AssuranceVoyage(models.Model):
    _name = 'assurfaz.voyage'
    _inherit = ['mail.thread']
    _description = 'Assurance Voyage'
  

    #passager
    pays_origine = fields.Char("Pays d'origine")
    pays_destination = fields.Selection([('senegal','Sénégal'),('ivoire','Côte d\'ivoire')],
        string="Pays de destination",
        default = 'senegal'
    )
    #Durée
    date_depart = fields.Date("Date de départ")
    date_retour = fields.Date("Date de retour")

    nb_passager = fields.Integer("Nombre de passagers")

    #Infos passagers
    date_naissance = fields.Date("Date de naissance du passager")
    age_passager = fields.Char("Âge du passager", compute="_get_passager_age")

    #Bénéficiaire
    name = fields.Many2one('res.partner',string="Nom du bénéficiaire",copy=False)
    civilite = fields.Selection([('monsieur','Monsieur'),
        ('madame','Madame')],
        string= 'Civilité ',
        default='madame'
    )

    choix_assureur = fields.Selection([('tous','TOUS'),
        ('axa','AXA'),('sunu','SUNU'),
        ('nsia','NSIA'),('sonam','SONAM')],
        string= 'Choix assureurs',
        default='axa'
    )

    state = fields.Selection([('nouvelle','Nouvelle'),
        ('validee','Validée'),
        ('acceptee','Acceptée'),
        ('refusee','Refusée')],
        default='nouvelle'
    )
    #periode de couverture
    duree_garantie= fields.Integer('Durée de la garantie en jours', compute="_get_duree_garantie")
    
    date_echeance = fields.Date("Date d'échéance", )

    #Modalités de remboursement
    modalite_remboursement= fields.Selection([('remboursable','Remboursable'),
        ('nonremboursable',' Non Remboursable')],
        string= 'Modalités de remboursement',
        default='nonremboursable'
    )

    prix_total = fields.Float("Montant total de l'assurance en CFA")
   
   

    @api.depends("date_naissance")
    def _get_passager_age(self):
        today_date = datetime.date.today()
        for pas in self:
            if pas.date_naissance:
                date_naissance = fields.Datetime.to_datetime( pas.date_naissance).date()
                age = str(int((today_date - date_naissance).days / 365))
                pas.age_passager = age + " ans"
            return pas.age_passager
               
           

    @api.depends("date_depart","date_retour")
    def _get_duree_garantie(self):
        for dur in self:
            if dur.date_depart:
                if dur.date_retour:
                    date_depart = fields.Datetime.to_datetime(dur.date_depart).date()
                    date_retour = fields.Datetime.to_datetime(dur.date_retour).date()
                    duree = int((date_retour - date_depart).days)
                    dur.duree_garantie = duree 
            return dur.duree_garantie


    @api.onchange("duree_garantie","date_depart")
    def onchange_date_echeance(self):
        date_depart= str(self.date_depart)
        if self.duree_garantie:
            date_depart = datetime.datetime.strptime(date_depart, "%Y-%m-%d")
            date_echeance = date_depart + relativedelta(days=self.duree_garantie) 
            self.date_echeance  = date_echeance.strftime("%Y-%m-%d")
    
   
    prime_id = fields.Many2one("assurfaz.prime")
    ref = fields.Char(default="Assurance Voyage")

    
    def action_accepte(self):
        for rec in self:
            rec.state = 'acceptee'
            new_prime = self.env['assurfaz.prime'].create(
                    {
                        
                        'prime': (self.prix_total * 10)/100,
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

