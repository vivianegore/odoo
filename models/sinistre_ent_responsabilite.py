from odoo import fields, models

class SinistreEntrepriseResponsabilite(models.Model):
    _name = 'sinistre.entreprise.responsabilite'
    _inherit = ['mail.thread']
    _description = 'Déclaration de sinistres responsabilité civive ou professionnels pour les entreprises'

    #type_sinistre_entreprise = responsabilite
    dommage_responsabilite_cause = fields.Selection([('vehicule','Véhicule endommagé'),
        ('objet','Objet endommagé'),('animal','Animaux blessés'),
        ('personne','Personnes blessées'),('fortune','Préjudice de fortune')],
        string = "Quel dommage a été causé?" , default = 'fortune'
    )
    #où est survenu le sinistre et quand? : date, localité, pays 
    
    appartenance_medicale =  fields.Selection([('oui','Oui'),
        ('non','Non')], string="Appartenez vous à un groupe professionnel soumis au secret médical?",default = 'non'
    )
    disposition =  fields.Selection([('oui','Oui'),
        ('non','Non')], string="Disposez-vous d\'une libération de l'obligation de garder le secret médical vis-à-vis de Assurfaz?",default = 'oui'
    )
    raison_declaration = fields.Selection([('confrontation','Confrontation par la patiente ou le patient'),
        ('avocat','Confrontation par l\'avocate/l\'avocat/l\'assurance de protection juridique'),
        ('autorite','Confrontation par les autorités'),('autre','Autre')],
        string = "Quelle est la raison de votre déclaration de cas?" , default = 'autorite'
    )
    #déroulement du sinistre : description_sinistre
    cas = fields.Selection([('personne','Personne'),
        ('animal','Animal')], string="le cas concerne-t-il une personne ou un animal?",default = 'personne'
    )
    reproche = fields.Selection([('erreur','Erreur de diagnostic'),
        ('traitement','Traitement inapproprié'),('information','Information insuffisante'),('autre','Inconnu/autre')], string="A quel reproche avez-vous dû faire face?",
        default = 'traitement'
    )
    animal_race = fields.Char("De quel animal s'agit-il?")
    responsable_sinistre = fields.Selection([('oui','Oui'),
        ('non','Non'),('partie','En partie'),('pas','Je ne sais pas')], string="Estimez-vous être responsable du sinistre?",default = 'pas'
    )
    justification = fields.Html("Veuillez justifier votre répons.")
    constat = fields.Selection([('oui','Oui'),
        ('non','Non'),('pas','Je ne sais pas')], string="Une constatation officielle a-t-elle eu lieu?",default = 'pas'
    )
    auteur_constat = fields.Char("Par qui?")
    etat_animal = fields.Selection([('blesse','Blessé'),
        ('decede','Décédé'),('pas','Je ne sais pas')], string="L'animal est ...",default = 'pas'
    )
    type_blessure = fields.Char("De quelles blessures l'animal souffre-t-il?")
    etat_personne = fields.Selection([('blesse','Blessée'),
        ('decede','Décédée'),('pas','Je ne sais pas')], string="La personne est ...",default = 'pas'
    )
    type_blessure_personne = fields.Html("Quelles blessures la personne a-t-elle subies")
    responsable_dommage = fields.Selection([('preneur','Preneur d\'assurance'),
        ('autre','Autre personne dans l\'entreprise'),('personne','Autre personne(extérieure à l\'entreprise)')], string="Qui a causé le dommage?",default = 'preneur'
    )
    #si responsable_dommage == autre afficher nom,prénom,fonction,téléphone sinon si la valeur est personne afficher qui a causé le dommage et pourquoi?
    nom_responsable_dommage = fields.Char("Nom du responsable du dommage")
    pnom_responsable_dommage = fields.Char("Prénom du responsable du dommage")
    telephone_responsable_dommage = fields.Char("Téléphone du responsable du dommage")
    fonction = fields.Char("Fonction dans l'entreprise")
    personne = fields.Html("Qui a causé le dommage et pourquoi?")

    #Qui nous déclare le sinistre?
    presentation = fields.Selection([('preneur','Preneur/preneuse d\'assurance'),('conseiller','Conseiller/consillère en assurance ou courtier/courtière'),
        ('autre','Autre personne')], string="Vous êtes... ", default='autre'
    )
    localite = fields.Char("Localité")
    #affichez les infos numero_police, nom,pnom,localite,npa,lieu,paays,telephone, email,civilité
    npa_personne = fields.Char("NPA du déclareur du sinistre")
    email_personne = fields.Char("Email du déclareur du sinistre")
    localite_personne = fields.Char("Localité du déclareur du sinistre")
    telephone_personne = fields.Char("Téléphone du déclareur du sinistre")
    name_personne = fields.Char("Nom du déclareur du sinistre")
    pname_personne = fields.Char("Prénom du déclareur du sinistre")

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
    