
from odoo import fields,models

     
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
    age_passager = fields.Integer("Âge du passager")

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
    duree_garantie= fields.Integer('Durée de la garantie en jours')
    date_effet = fields.Date("Date d'effet")
    date_echeance = fields.Date("Date d'échéance")

    #Modalités de remboursement
    modalite_remboursement= fields.Selection([('remboursable','Remboursable'),
        ('nonremboursable','Remboursable')],
        string= 'Modalités de remboursement',
        default='nonremboursable'
    )
  