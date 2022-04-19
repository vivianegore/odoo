from odoo import fields, models

class SinistreEntreprisetechnique(models.Model):
    _name = 'sinistre.entreprise.technique'
    _inherit = ['mail.thread']
    _description = 'Déclaration de sinistres assurances techniques pour les entreprises'

    cas_annonce = fields.Char("Qui a annoncé le cas?")
    nom_agent = fields.Char("Nom de l'agent")
    dommage_cause = fields.Html("Veuillez énumérer les dommages")
    declaration_police = fields.Html("Auprès de quel poste de police?")
    dommage = fields.Html("Quel dommage a été causé?")
    prix_dommage =fields.Selection([('500000','< 500 000CFA'),
        ('1000000','> 1000 000CFA'), ('entre','500 000 CFA et  1000 000CFA')], 
        string="A combien estimez-vous le dommage?"
    )

    preneur= fields.Selection([('oui','Oui'),
        ('non','Non')], string="Etes-vous le preneur d'assurance?",default = 'non'
    )
    #si non
    presentation_personne = fields.Selection([('conseiller','Conseiller en assurance ou courtier'),
        ('autre','Autre personne')], string="Vous êtes... "
    )
    name = fields.Char("Votre nom ")
    pname= fields.Char("Votre prénom ")
    adresse = fields.Char("Votre adresse")
    email = fields.Char("Votre  email")
    npa = fields.Char("Votre npa")
    
    #conseiller
    entreprise = fields.Char("Le nom de votre entreprise")
    #autre
    telephone = fields.Char("Votre numéro de téléphone")
    npa_preneur = fields.Char("NPA")

    #Quel est le numéro de police?
    numero_police = fields.Char("Numéro de police")

    #preneur d'assurance
    formule_appel = fields.Selection([('madame','Madame'),
        ('monsieur','Monsieur'),('entreprise','Entreprise')], string="Titre de civilité " , default="monsieur"
    )
    civilite = fields.Selection([('madame','Madame'),
        ('monsieur','Monsieur')], string="Formule d'appel", default="monsieur"
    )
    # si entreprise est sélectionné, en plus de son formulaire on ajoute une Personne de contact
    #Personne en contact
    name_personne_contact= fields.Char("Nom de la personne de l'entreprise en contact avec nous ")
    pname_personne_contact= fields.Char("Prénom de la personne de l'entreprise en contact avec nous ")
    adresse_personne_contact = fields.Char("Adresse de la personne de l'entreprise en contact avec nous")
    email_personne_contact = fields.Char("Email de la personne de l'entreprise en contact avec nous")
    npa_personne_contact = fields.Char("Npa de la personne de l'entreprise en contact avec nous")
    telephone_personne_contact = fields.Char("Numéro de téléphone de la personne de l'entreprise en contact avec nous")
    npa_societe = fields.Char("NPA")
    email_societe = fields.Char("Email")
    localite_societe = fields.Char("Localité")
    telephone_societe = fields.Char("Téléphone")
    description_sinistre = fields.Html("Veuillez décrire le déroulement")
    date_fait = fields.Date ("Quand le sinistre s’est-il produit?")
    localite_sinistre = fields.Char("Où le sinistre s'est-il produit?")
    pays_sinistre= fields.Char("Pays où le sinistre s'est produit")

    state = fields.Selection([('cours','En cours'),
        ('traite','Traitée'),('rejete','Rejetée')],
        default='cours'
    )

   
    def action_traite(self):
        for rec in self:
            rec.state = 'traite'

    def action_retour(self):
        for rec in self:
            rec.state = 'cours'
    
    def action_rejete(self):
        for rec in self:
            rec.state = 'rejete'