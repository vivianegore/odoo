from odoo import api,fields, models,_
import datetime
from dateutil.relativedelta import *
from odoo.exceptions import UserError

class AssuranceAuto(models.Model):
    _name = 'assurfaz.auto'
    _description = 'Assurance Auto/moto'

   

    @api.onchange("duree_garantie","date_effet")
    def onchange_date_echeance(self):
        date_effet= str(self.date_effet)
        if self.date_effet:
            date_effet = datetime.datetime.strptime(date_effet, "%Y-%m-%d")
            date_echeance = date_effet + relativedelta(months=self.duree_garantie) 
            self.date_echeance  = date_echeance.strftime("%Y-%m-%d")
    
    @api.onchange('assurance_type')
    def verification(self):
        if self.assurance_type =='vehicule':
            if len(self.vehicule_ids) > 1:
                raise UserError(_("Vous ne pouvez enregistrer qu'un seul véhicule pour ce type d'assurance "))
        else:
            if len(self.vehicule_ids) > self.nombre_vehicule:
                raise UserError(_("Vous devez enregistrer exactement le nombre de véhicules défini pour ce type d'assurance "))

   
    #Bénéficiaire
    name = fields.Many2one('res.users',string="Nom du bénéficiaire",copy=False)
    civilite = fields.Selection([('monsieur','Monsieur'),
        ('madame','Madame')],
        string= 'Civilité ',
        default='madame'
    )
    
    choix_assureur = fields.Selection([('tous','TOUS'),
        ('axa','AXA'),('amsa','AMSA'),
        ('askia','ASKIA'),('sunu','SUNU'),
        ('nsia','NSIA'),('cnart','CNART')],
        string= 'Choix assureurs',
        default='amsa'
    )
    assurance_type= fields.Selection([('vehicule','Véhicule individuel'),
        ('flotte','Flotte automobile')],
        string= 'Vous souhaitez une assurance pour ',
        default='vehicule'
    )
    state = fields.Selection([('Nouvelle','Nouvelle'),
        ('Reçue','Reçue'),
        ('Acceptee','Acceptée'),
        ('Vendue','Vendue'),
        ('Annulee','Annulée')],
        default='Nouvelle'
    )
    #periode de couverture
    duree_garantie= fields.Integer('Durée de la garantie en mois')
    date_effet = fields.Date("Date d'effet")
    date_echeance = fields.Date("Date d'échéance")
    nombre_vehicule = fields.Integer('Nombre de vehicule')

    garantie_ids = fields.One2many('assurfaz.auto.garantie',"assurance_auto_id")
    vehicule_ids = fields.One2many('assurfaz.auto.vehicule',"assurance_auto_id")
    


    
   
           