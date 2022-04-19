from odoo import fields, models

class SinistreParticulierAccident(models.Model):
    _name = 'sinistre.particulier.accident'
    _inherit = ['mail.thread']
    _description = 'Déclaration de sinistres'
    
    #type_sinistre_particulier == accident
    secteur_activite =  fields.Selection([('assurance','Assurance-accidents'),('journaliere','Indemnité journalière en cas de maladie'),
        ('cadre','Cadre management'),('indemnite','Indemnité d\'accouchement'),
        ('convention','Assurance par convention'),('complementaire','Assurance complémentaire LAAC(envoyer la copie de votre déclaration de sinistre à la Suva ou un autre assureur')],
        string="Sélectionnez le secteur d'activité", default='assurance'
    )
    #secteur_activité == assurance, convention
    branche_assurance =  fields.Selection([('non','Accident non professionnel'),('maladie','Accident / maladie professionnel/le'),
        ('visiteur','Assurance visiteurs(dans tous les formulaires)')],
        string="Sélection de la branche d'assurance", default='visiteur'
    )
    nature_sinistre =  fields.Selection([('incapacite','Incapacité de travail jusqu\'à 2 jours'),('plus','Incapacité de travail jusqu\'à 3 jours ou plus'),
        ('rechute','Rechute')],
        string="Sélection de la nature du sinistre", default='incapacite'
    )
    #information sur l'employeur
    numero_police = fields.Char("Numéro de police")
    entreprise = fields.Char("Le nom de votre entreprise")
    filiale = fields.Char("Filiale/service")
    personne_contact = fields.Char("Personne de contact")
    npa_societe = fields.Char("NPA")
    email_societe = fields.Char("Email")
    localite_societe = fields.Char("Localité")
    telephone_societe = fields.Char("Téléphone")
    #npa , lieu, telephone, email
    #Coordonnées de paiement(IBAN)
    coordonnee_paiement = fields.Char("Coordonnées de paiement(IBAN)")
    coordonnee_paiement_personne = fields.Char("Coordonnées de paiement(IBAN)")


    #Personne assurée
    #civilité, nom, pnom
    etat_civil = fields.Selection([('celibataire','Célibataire'),('marie','Marié'),
        ('partenariat','Partenariat enregistré'),('divorce','Divorcé'),
        ('veuf','Veuf / veuve')], string="Etat civil",
        default='celibataire'
    )
    nationalite = fields.Char("Nationalité")
    date_naissance = fields.Date("Date de naissance ")
    # npa, lieu, pays, telephone , email,,coordonnee_paiemeent
    impot = fields.Selection([('oui','Oui'),('non','Non')],
        string = "Soumis à l'impôt à la source", default='non'
    )
    #Contrat d'engagement
    date_engagement = fields.Date("Date d'engagement")
    profession = fields.Char("Profession")
    fonction = fields.Selection([('employe','Employé/travailleur'),('moyen','Cadre moyen'),
        ('superieur','Cadre supérieur'),('apprenti','Apprenti'),('stagiaire','Stagiaire')],
        string = "Fonction professionnelle", default='stagiaire'
    )
    contrat_type = fields.Selection([('cdi','Contrat à durée indéterminée'),('cdd','Contrat à durée déterminée'),
         ('resilie','Contrat de travail résilié')], string = "Rapport de travail",
        default='cdd'
    )
    lieu_travail =  fields.Selection([('usine','En usine/en atelier'),('service','Service technique'),
       ('bureau','Employé de bureau'),('vente','Vente'),
        ('autre','Autres')], string = "Lieu de travail habituel",
        default='service'
    )
    connaissance_travail = fields.Selection([('qualifie','Travail qualifié'),('non','Travail non qualifié'),
       ('semi','Travail semi-qualifié'),('apprenti','Apprenti'),
        ('inconnu','Inconnu')], string = "Connaissances professionnelles",
        default='non'
    )
    occupation = fields.Selection([('reguliere','Régulière'),('irreguliere','Irrégulière'),
       ('partiel','Chômage partiel'),('intermediaire','Salaire intermédiaire'),
        ('inconnu','Inconnu')], string = "Occupation",
        default='irreguliere'
    )
    temps_travail = fields.Integer( "Temps de travail en Heure/semaine")
    degre_occupation = fields.Float("Dégré d'occupation contactuel en %")
    horaire_travail = fields.Integer("Horaire de travail habituel dans votre entreprise en Heure/Semaine")

    description_sinistre = fields.Html("Veuillez décrire le déroulement")
    date_fait = fields.Date ("Quand le sinistre s’est-il produit?")
    localite_sinistre = fields.Char("Où le sinistre s'est-il produit?")
    pays_sinistre= fields.Char("Pays où le sinistre s'est produit")

    dommage_declare = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Le dommage a-t-il été déclaré à la police?",default = 'non'
    )
    declaration_police = fields.Html("Auprès de quel poste de police?")
    titre = fields.Selection([('personnel','Particulier'),('societe','Entreprise')],
        string="Statut", default = 'personnel'
    )
    
    origine_accident = fields.Char("Qui ou Quoi est à l'origine de l'accident?")
    partie = fields.Selection([('tete','Tête'),('yeux','Yeux '),
        ('cou','Cou'),('machoire','Mâchoire '),('oreille','Oreilles(appareils auditifs)'),
        ('dent','Dents '),('bras','Bras/coude/main'),
        ('doigt','Doigts '),('corps','Corps'),('ventre','Ventre'),('organes','Organes génitaux '),
        ('dos','Dos'),('epaule','Epaule'),('thorax','Thorax / côtes'),
        ('vertebrale','Colonne vertébrale'),('jambe','Jambe/pied'),
        ('genou','Genou '),('orteil','Orteils'),('crane','Crâne cervau '),
        ('autre','Autres/ voir données complémentaires'),('inconnu','Inconnu')],
        string = "Partie du corps touchée", default = 'dos'
    )
    cote =  fields.Selection([('gauche','Gauche'),('droit','Droit')],
        string = "Quel côté?", default='droit'
    )
    lesion = fields.Selection([('morsure','Morsure'),('entorse','Entorse '),
        ('fracture','Fracture'),('inflammation','Inflammation '),('corps','Corps étranger'),
        ('contusion','Contusion '),('forte','Contusion forte'),
        ('fissure','Fêlure/fissure '),('coupure','Coupure'),('egratignure','Egratignure'),('balle','Blessures par balle '),
        ('enflure','Enflure'),('foulure','Foulure'),('piqure','Piqûre'),
        ('deboitement','Déboîtement/désarticulation'),('brulure','Brûlure par abrasif'),
        ('intoxication','Intoxication '),('luxation','Luxation'),('dechirure','Déchirure de muscles '),
        ('autre','Autres/ voir données complémentaires'),('indetermine','Idéterminé')],
        string = "Lésion/blessure", default = 'entorse'
    )
    donnee_complementaire = fields.Html("Données complémentaires")
    dernier_jour = fields.Char("Dernier jour de travail avant l'acident")
    Heure = fields.Char("Heure")
    motif_absence = fields.Selection([('accident','Accident'),('vacance','Vacances '),
        ('maladie','Maladie'),('service','Service militaire '),('conge','Congés non payés'),
        ('chomage','Chômage '),('contrat','Contrat de travail dénoncé'),
        ('autre','Autres')],
        string = "motifs d'abscence prolongée", default = 'maladie'
    )

    #médécin/hôpital
    debut_traitement = fields.Date("Début du traitement médical")
    hopital = fields.Char("Hôpital/clinique")
    medecin_traitant = fields.Char("Médécin traitant") #npa, lieu, pays, telephone

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
    npa_personne = fields.Char("NPA du déclareur du sinistre")
    email_personne = fields.Char("Email du déclareur du sinistre")
    localite_personne = fields.Char("Localité du déclareur du sinistre")
    telephone_personne = fields.Char("Téléphone du déclareur du sinistre")
    pays_personne= fields.Char("Pays")
    ville_personne= fields.Char("Ville")

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