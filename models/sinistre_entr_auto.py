from odoo import fields, models

class SinistreEntrepriseAutomobile(models.Model):
    _name = 'sinistre.entreprise.automobile'
    _inherit = ['mail.thread']
    _description = 'Déclaration de sinistres automobiles pour les entreprises'

    cause_sinistre_automobile= fields.Selection([('accident','Accident de la circulation / collision'),
        ('bris','Bris de glace'),
        ('vol','Vol / Effraction'),('incendie','Incendie, incendie électrique,foudre,explosion'),
        ('collision','Collision avec un véhicule prêté')],
        string = "Cause du sinistre" , default = 'accident'
    )
    #type_sinistre_particulier == automobiles
    #demande d'information
    info = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Quelqu'un a-til été blessé?", default = 'oui'
    )
    blessure_description = fields.Html("Décrivez la blessure")
    info2 = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Votre véhicule a-t-il été endommagé?",default = 'oui'
    )
    marque = fields.Char("Marque/Type")
    plaque_controle = fields.Char("Plaque de contrôle")
    marque_autre_vehicule = fields.Char("Marque/Type")
    plaque_controle_autre_vehicule = fields.Char("Plaque de contrôle")
    dommage = fields.Html("Quel dommage a été causé?")
    prix_dommage =fields.Selection([('500000','< 500 000CFA'),
        ('1000000','> 1000 000CFA'), ('entre','500 000 CFA et  1000 000CFA')], 
        string="A combien estimez-vous le dommage?"
    )
    prix_dommage_chose =fields.Selection([('500000','< 500 000CFA'),
        ('1000000','> 1000 000CFA'), ('entre','500 000 CFA et  1000 000CFA')], 
        string="A combien estimez-vous le dommage?"
    )
    conducteur = fields.Selection([('vous','Vous-même'),
        ('connaissance','Une connaissance'), ('autre','Une personne que vous ne connaissez pas')], 
        string="Qui conduisait le véhicule?", default = 'autre'
    )
    accident = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Un autre véhicule a-t-il été endommagé?",default = 'oui'
    )
    chose_endommage = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Des choses emportées dans votre véhicule ont-elles été endommagées?",default = 'oui'
    )
    #si oui : 
    description_chose = fields.Html("Quelles choses emportées dans votre véhicule ont été endommagées?")

    #si on choisit une personne que vous ne connaissez pas 
    name_conducteur= fields.Char("Nom du conducteur")
    pname_conducteur = fields.Char("Prénom du conducteur")
    adresse_conducteur = fields.Char("Adresse du conducteur")
    email_conducteur = fields.Char("Adresse email du conducteur")
    pays_conducteur = fields.Char("Pays du conducteur")
    date_naissance = fields.Date("Date de naissance ")
    date_permis = fields.Char("Permis de conduire délivré le ")

 
    description_sinistre = fields.Html("Veuillez décrire le déroulement")
    date_fait = fields.Date ("Quand le sinistre s’est-il produit?")
    localite_sinistre = fields.Char("Où le sinistre s'est-il produit?")
    pays_sinistre= fields.Char("Pays où le sinistre s'est produit")
    pays_personne= fields.Char("Pays")
    ville_personne= fields.Char("Ville")
    # Où et quand les faits se sont-ils passés?
    

    #Selon vous, êtes-vous responsable de l'accident?
    responsable_accident = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Selon vous, êtes-vous responsable de l'accident?",default = 'oui'
    )
    dommage_declare = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Le dommage a-t-il été déclaré à la police?",default = 'oui'
    )
    declaration_police = fields.Html("Auprès de quel poste de police?")
    
    preneur= fields.Selection([('oui','Oui'),
        ('non','Non')], string="Etes-vous le preneur d'assurance?",default = 'non'
    )
    #si non
    presentation_personne = fields.Selection([('conseiller','Conseiller en assurance ou courtier'),
        ('autre','Autre personne')], string="Vous êtes... ", default='autre'
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
