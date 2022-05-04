from unittest import result
from odoo import fields,models,_,api
from odoo.exceptions import  UserError
import datetime
from dateutil.relativedelta import *
     
class AssuranceHabitation(models.Model):
    _name = 'assurfaz.habitation'
    _inherit = ['mail.thread']
    _description = 'Assurance Habitation'
    _rec_name = 'type_logement'
  

    name = fields.Char('Nom')
    type_logement= fields.Selection([('appartement','Appartement'),
        ('maison','Maison(max R+2)'),('immeuble','Immeuble')],
        string= 'Vous souhaitez une assurance pour  ',
        default='maison'
    )

    #Superficie & Nombre de pièces
    surface = fields.Char('Surface développée en m²')
    nb_piece = fields.Integer('Nombre de pièces')

    #Détails du logement 
    type_toiture= fields.Selection([('tuile','Tuile(Ardoise)'),
        ('tole','Tôle métale'),('beton','Béton'),('paille','Paille')],
        string= 'Type de toiture ',
        default='tuile'
    )
    environnement_immediat= fields.Selection([('residentiel','Quartier résidentiel'),
        ('chantier','Chantiers à proximité'),('prochelieu','Proche Usine/Station Essence/Marché')],
        string= 'Environnement immédiat ',
        default='chantier'
    )
    adresse = fields.Char('Adresse du logement ')

    choix_assureur = fields.Selection([('tous','TOUS'),
        ('axa','AXA'),('amsa','AMSA'),
        ('askia','ASKIA'),('sunu','SUNU'),
        ('nsia','NSIA'),('cnart','CNART')],
        string= 'Choix assureurs',
        default='amsa'
    )
    state = fields.Selection([('nouvelle','Nouvelle'),
        ('validee','Validée'),
        ('acceptee','Acceptée'),
        ('refusee','Refusée')],
        default='nouvelle'
    )

    #Propriétaire/Locataire 
    occupant = fields.Selection([('locataire','Locataire'),
        ('proprietaire','Propriétaire occupant')],
        string= 'Propriétaire/Locataire  ',
        default='proprietaire'
    )

    #Montant du loyer
    loyer_locataire = fields.Float('Montant du loyer en CFA')

    #Valeur 
    valeur_garantie = fields.Float('Valeur du contenu à garantir en CFA')
    valeur_batiment= fields.Float('Valeur du bâtiment en CFA')

    #periode de couverture
    duree_garantie= fields.Integer('Durée de la garantie en mois')
    date_effet = fields.Date("Date d'effet")
    date_echeance = fields.Date("Date d'échéance")

    mt_total = fields.Float("Montant total de l'assurance en CFA")
   

    

    @api.onchange('duree_garantie','date_effet')
    def onchange_date_echeance(self):
        date_effet= str(self.date_effet)
        if self.date_effet:
            date_effet = datetime.datetime.strptime(date_effet, "%Y-%m-%d")
            date_echeance = date_effet + relativedelta(months=self.duree_garantie) 
            self.date_echeance  = date_echeance.strftime("%Y-%m-%d")

    prime_id = fields.Many2one("assurfaz.prime")
    ref = fields.Char(default="Assurance Habitation")

    
    def action_accepte(self):
        for rec in self:
            rec.state = 'acceptee'
            new_prime = self.env['assurfaz.prime'].create(
                    {
                        
                        'prime': (self.mt_total * 10)/100,
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
