from odoo import fields, models

class SinistreParticulierPaiement(models.Model):
    _name = 'sinistre.particulier.paiement'
    _inherit = ['mail.thread']
    _description = 'Déclaration de sinistres paiement pour les particuliers'

     #type_sinistre_particulier == paiement
    
    nom_entreprise = fields.Char("Nom de l'entreprise")
    nom_compagnie = fields.Char("Nom de l'entreprise")
    entreprise_nom = fields.Char("Nom de l'entreprise")

    evenement = fields.Selection([('maladie','Maladie'),('accident','Accident '),('chomage','Chômage')],
        string = "Pour quel événement assuré avez-vous besoin d’une protection des paiements?", default = 'chomage'
    )
    #evenement == maladie ou accident
    date_debut = fields.Date("Depuis quand êtes-vous en incapacité de travail?")
    degre_incapacite = fields.Integer("Selon le certificat médical, quel est votre degré d’incapacité de travail en %? ")
    nom_employeur = fields.Char("Auprès de quel employeur étiez-vous en activité à la survenance de l’incapacité de travail? ")
    localite_employeur = fields.Char(" Localité de l'employeur")
    telephone_employeur = fields.Char("Numéro de téléphone de l'employeur")
    date_embauche = fields.Date("Depuis quand êtes-vous en poste chez cet employeur?")
    time_travail = fields.Integer("Quelle est votre temps de travail moyen?")
    
    date_traitement_medical = fields.Date("Quand le traitement médical a-t-il débuté?")
    specialiste = fields.Char("Par quels spécialistes et dans quels établissements (clinique, hôpital) êtes-vous ou avez-vous été soigné(e)?")
    nom_medecin_traitant = fields.Char("Nom du/de la médecin traitant(e)")
    localite_medecin_traitant = fields.Char("Localité du/de la médecin traitant(e)")
    numero_medecin_traitant = fields.Char("Numéro de téléphone du/de la médecin traitant(e)")
    question_medecin_traitant = fields.Selection([('oui','Oui'),('non','Non ')],
        string = "Avez-vous d’autres médecins traitant(e)s? ", default = 'non'
    )
    #si oui
    info_medecin_traitant = fields.Char("Veuillez saisir le nom et l’adresse:")
    question_info_maladie = fields.Selection([('oui','Oui'),('non','Non ')],
        string = "Votre incapacité de travail actuelle résulte-t-elle d’une maladie antérieure / d’un accident antérieur?", 
        default = 'non'
    )
    #si oui
    date_debut_maladie = fields.Date("Quand ce trouble de la santé a-t-il été diagnostiqué pour la première fois?")
    description_maladie = fields.Html("Veuillez décrire la maladie antérieure / l’accident antérieur.")
    question_info_trouble = fields.Selection([('oui','Oui'),('non','Non ')],
        string = "Votre incapacité de travail actuelle résulte-t-elle de troubles dorsaux, cervicaux ou plus généralement de la colonne vertébrale, ou résulte-t-elle d’une pathologie psychique?", 
        default = 'non'
    )
    #evenement == accident
    date_accident = fields.Date("Quand l’accident s’est-il produit? ")
    heure_approximative = fields.Char("Heure approximative")
    lieu_accident = fields.Char("Lieu de l’accident")
    description_accident = fields.Html("Veuillez décrire en détail le déroulement de l’accident (nature de la lésion, diagnostic, parties du corps concernées, etc.)")
    nom_assurance = fields.Char("Quelle est votre assurance-accidents?")
    numero_police_assurance = fields.Char("Numéro de police de votre assurance accident")
    question_info_assurance = fields.Selection([('oui','Oui'),('non','Non ')],
        string = "Avez-vous déjà annoncé votre accident à votre assurance-accidents? ", 
        default = 'non'
    )
    #si oui
    numero_reference = fields.Char("Quel est le numéro de référence du cas de sinistre?")

    question_info_rapport = fields.Selection([('oui','Oui'),('non','Non ')],
        string = "Un rapport de police a-t-il été établi ou une procédure pénale a-t-elle été engagée?", 
        default = 'non'
    )
    #si oui
    service_competent = fields.Char("Veuillez indiquer le service de police compétent.")
    
    """ document = fields.Binary("Joindre votre document")
    nom_document = fields.Char("Nom du document") """
    #preneur
    #numero_police
    #formulaire de coordonnées
    coordonnee_paiement = fields.Char("Coordonnées de paiement(IBAN)")
    nom_titulaire_compte = fields.Char("Nom et prénom du/de la titulaire du compte")
    localite_titulaire_compte = fields.Char("Localité du/de la titulaire du compte")
    divers = fields.Html("Souhaitez-vous ajouter quelque chose?")

    #evenement == maladie
    description_maladie = fields.Html("Veuillez décrire en détail la nature de l’inffection dont vous souffrez et le diagnostic.")
    question_assurance_maladie = fields.Selection([('oui','Oui'),('non','Non '),('pas','Je ne sais pas ')],
        string = "Percevez-vous des indemnités journalières d’une assurance d’indemnité journalière en cas de maladie?", 
        default = 'non'
    )
    #si oui
    nom_assurance_maladie = fields.Char("Quelle est votre assurance d’indemnité journalière en cas de maladie?")
    police_numero_maladie = fields.Char("Police n° ")
    reference_cas = fields.Char("Référence du cas ")

    #document
    #nom_document
    #preneur
    #numero_police
    #formulaire de coordonnées
    #coordonnee_paiement

    #evenement == chomage
    date_fin = fields.Char("Date de la fin des rapports de travail ")
    #nom_employeur 
    #infos employeur
    fin_rapport_travail = fields.Selection([('employeur','Mon employeur'),('moi','Moi-même ')],
        string = "Qui a mis fin aux rapports de travail?", 
        default = 'moi'
    )
    date_licenciement = fields.Date("Quand le licenciement a-t-il eu lieu (date de la lettre de licenciement)?")
    #si employeur est sélctionné
    cause_licenciement = fields.Html("Merci de décrire les causes qui ont entraîné votre licenciement:")
    question_licenciement = fields.Selection([('oui','Oui'),('non','Non ')],
        string = "Le licenciement a-t-il eu lieu pendant une période d’essai, d’apprentissage ou de formation? ", 
        default = 'oui'
    )

    contrat_type = fields.Selection([('cdi','Contrat à durée indééterminée'),('cdd','Conrat à durée déterminée '),('saisonnier','Contrat saisonnier'),
    ('activite','Activité lucrative indépendante ')],
        string = "Quel type de rapports de travail aviez-vous auprès de votre ancien employeur? ", 
        default = 'cdi'
    )
    question_chomage = fields.Selection([('complet','Chômage complet'),('partiel','Chômage partiel ')],
        string = "S’agit-il d’un cas de chômage complet ou partiel?", 
        default = 'partiel'
    )
    temps_moyen = fields.Integer("Quel était votre temps de travail moyen dans votre dernier poste?")
    question_indemnite = fields.Selection([('oui','Oui'),('non','Non '),('pas','Je ne sais pas ')],
        string = "Avez-vous droit à une indemnité de chômage de l’assurance-chômage? ", 
        default = 'non'
    )
    #si oui ou pas
    question_cas_signale = fields.Selection([('oui','Oui'),('non','Non ')],
        string = "Le cas de chômage a-t-il été annoncé auprès de votre commune de résidence ou de l’office régional de placement (ORP) compétent? ", 
        default = 'oui'
    )
    #si oui
    question_suspension = fields.Selection([('oui','Oui'),('non','Non ')],
        string = "Des journées de suspension ont-elles été prononcées? ", 
        default = 'oui'
    )
    orp = fields.Char("Merci d’indiquer l’ORP dont vous dépendez ou votre caisse d’assurance-chômage.")
    #la fin comme pour les autres

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