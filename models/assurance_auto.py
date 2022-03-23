from odoo import api,fields, models,_
import datetime
from dateutil.relativedelta import *

from odoo.addons.mail.models import res_users


class AssuranceAuto(models.Model):
    _name = 'assurfaz.auto'
    _inherit = ['mail.thread']
    _description = 'Assurance Auto/moto'

   

    @api.onchange("duree_garantie","date_effet")
    def onchange_date_echeance(self):
        date_effet= str(self.date_effet)
        if self.date_effet:
            date_effet = datetime.datetime.strptime(date_effet, "%Y-%m-%d")
            date_echeance = date_effet + relativedelta(months=self.duree_garantie) 
            self.date_echeance  = date_echeance.strftime("%Y-%m-%d")
   
  

   
    #Bénéficiaire
    name = fields.Many2one('res.partner',string="Nom du bénéficiaire",copy=False)
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
    state = fields.Selection([('nouvelle','Nouvelle'),
        ('validee','Validée'),
        ('acceptee','Acceptée'),
        ('refusee','Refusée')],
        default='nouvelle'
    )
    #periode de couverture
    duree_garantie= fields.Integer('Durée de la garantie en mois')
    date_effet = fields.Date("Date d'effet")
    date_echeance = fields.Date("Date d'échéance")
    nombre_vehicule = fields.Integer('Nombre de vehicule')

    garantie_ids = fields.One2many('assurfaz.auto.garantie',"assurance_auto_id")
    vehicule_ids = fields.One2many('assurfaz.auto.vehicule',"assurance_auto_id")

    carte_grise = fields.Binary(string="Carte grise")
    

    def notification_send(self):
        notification_ids=[]
        if self.env.user:
            notification_ids.append((0,0,{
                    'res_partner_id': self.env.user.partner_id.id,
                    'notification_type' : 'inbox'
   
            }))

            self.env['mail.message'].create({

                'message_type':"notification",
                'body': "Message",
                'subject': "Message subject",
                'model': self._name,
                'res_id':self.id,
                'partner_ids': [self.env.user.partner_id.id],
                'author_id': self.env.user.partner_id.id,
                'notification_ids': notification_ids,
            })
           





    
   
           