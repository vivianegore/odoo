from odoo import fields, models

class SinistreParticulierResponsabilite(models.Model):
    _name = 'sinistre.particulier.responsabilite'
    _inherit = ['mail.thread']
    _description = 'Déclaration de sinistres responsabilite pour les particuliers'


    dommage_sinistre_responsabilite = fields.Selection([('accident','Accident de la circulation avec véhicule prêté'),
        ('dommage','Dommage causé en tant que locataire'),('autre','Autre dommage')],
        string="De quel dommage s’agit-il?" , default='dommage'
    )
    situation = fields.Selection([('demenage','Je déménage'),
        ('deja','J\'ai déjà déménagé'),('demenagepas','Je ne déménage pas')],
        string="Votre situation" , default='deja'
    )
    objet_loue_dommage = fields.Selection([('plusieurs','Plusieurs sinistres se sont produits'),
        ('seul','Il n\'y a eu qu\'un seul sinistre'),('pas','Je ne sais pas')],
        string="Dommages à l'objet loué" , default='plusieurs'
    )
    date_fait = fields.Date ("Quand le sinistre s’est-il produit?")
    #infos relative à l'objet
    #adresse
    #npa
    date_emmenagement = fields.Date("Quand avez-vous emménagé?")
    date_demenagement = fields.Date("Quand avez-vous déménagé?")

    #informations relatives au sinistre
    repare_dommage = fields.Selection([('oui','Oui'),
        ('non','Non')],
        string="Le dommage est-il réparé?" , default='oui'
    )
    bailleur_info = fields.Selection([('oui','Oui'),
        ('non','Non')],
        string="Avez-vous informé le bailleur du sinistre?" , default='oui'
    )
    dommage_locataire = fields.Html("Veuillez indiquer ce qui a été endommagé dans le logement")
    #prix dommage
    document =  fields.Selection([('entree','Etat des lieux d\'entrée'),
        ('sortie','Etat des lieux de sortie'),('decompte','Décompte des dommages')],
        string = "Parmis les documents suivants, desquels disposez-vous?" , default='sortie'
    )
    #numéro de police
    #information preneur
    auteur_declaration_sinistre = fields.Selection([('preneur','Preneur d\'assurance'),
        ('courtier','Courtier'),('bailleur','Bailleur'),('autre','Autre')],
        string = "Qui déclare le sinistre?" , default='preneur'
    )
    # si courtier ou autre : entreprise, nom, telephone à afficher
    #Lésé: coordonnées du bailleur
    titre = fields.Selection([('personnel','Particulier'),('societe','Entreprise')],
        string="Statut", default = 'personnel'
    )
    
    # particulier: nom, pnom, telephone, npa, lieu, email, numero
    #entreprise: entreprise, telephone, npa , lieu, email, numero
    numero = fields.Char("Numéro")

        #responsabilite_dommage == accident de la circulation avec véhicule prêté
    fait_passe = fields.Selection([('vehicule','Véhicule conduit'),
        ('chose','Autre chose'),('deux','Les deux')],
        string = "Qu'est-ce qui a été endommagé?" , default='deux'
    )
    
    sinistre_provoque = fields.Selection([('oui','Oui'),
        ('non','Non')],
        string="Le sinistre a-t-il été provoqué par une collision?" , default='oui'
    )
    responsable_sinistre= fields.Selection([('oui','Oui'),
        ('non','Non'),('pas','Je ne sais pas')], string="Estimez-vous être responsable du sinistre?",default = 'non'
    )
    usage_vehicule = fields.Selection([('prive','A titre privé'),('professionnel','A titre professionnel')], 
        string="A quel titre avez-vous utilisé le véhicule endommagé?",default = 'prive'
    )
    nb_jour = fields.Integer("Combien de jours avez-vous utilisé le véhicule durant l'année civile en cours?")
    paiement = fields.Selection([('oui','Oui'),
        ('non','Non')],
        string="Avez-vous dû payer pour utiliser le véhicule?" , default='oui'
    )
    
    localisation_sinistre = fields.Selection([('residence','A mon adresse de résidence'),
        ('autre','A une autre adresse'),('etranger','A l\'etranger')], string="Où le sinistre s'est-il produit?",
        default = 'etranger'
    )
    
    pays_sinistre= fields.Char("Pays où le sinistre s'est produit")
    lieu_sinistre = fields.Selection([('domicie','Au domicile'),
        ('hors','Hors du domicile')], string="Lieu du sinistre? ", default = 'domicie'
    )
    localite_sinistre = fields.Char("Où le sinistre s'est-il produit?")
    description_sinistre = fields.Html("Veuillez décrire le déroulement")
    #infos véhicule
    type_vehicule = fields.Selection([('tourisme','Voiture de tourisme'),
        ('camionnette','Camionnette'),('moto','Moto'),
        ('remorque','Remorque'),('autre','Autre')],
        string="De quel type de véhicule s'agit-il?" , default='moto'
    )
    marque_vehicule = fields.Char("Marque/type")
    #plaque_controle 
    assurance_vehicule = fields.Selection([('non','Non'),
        ('partiellement','Oui, partiellement'),('completement','Oui, complètement'),
        ('pas','Je ne sais pas ')],
        string="Le véhicule est-il couvert par une assurance?" , default='completement'
    )
    compagnie = fields.Selection([('assurfaz','ASSURFAZ'),
        ('autre','Autre')],
        string="Auprès de quelle compagnie?" , default='assurfaz'
    )
    #si autre, nom de la compagnie est renseignée
    compagnie_name = fields.Char("Compagnie")
    volant_personne = fields.Selection([('preneur','Preneur d\'assurance'),
        ('autre','Autre personne assurée')],
        string="Qui était au volant du  véhicule?" , default='preneur'
    )
    personne_menage = fields.Boolean("La personne fait partie de mon ménage")
    nom_autre = fields.Char("Nom de la personne")
    pnom_autre = fields.Char("Prénom de la personne")
    npa_autre = fields.Char("NPA de la personne")
    email_autre = fields.Char("Email de la personne")
    localite_autre = fields.Char("Localité de la personne")
    telephone_autre = fields.Char("Téléphone de la personne")
    date_naissance = fields.Date("Date de naissance ")
    #prenom,nom,date_naissance, personne_menage, numero, npa, lieu, telephone
    #Lésé: coordonnées du bailleur

        #responsabilite_dommage == autre
    raconte_fait = fields.Selection([('accident','Accident de vélo'),
        ('enfant','Mon enfant a provoqué un dommage'),('animal','Mon animal a provoqué un dommage'),
        ('objet','Un objet prêté a été cassé'),('autre','Autre')],
        string = "Que s'est-il passé?" , default='enfant'
    )
    dommage_autre = fields.Selection([('vehicule','Véhicule'),
        ('batiment','Bâtiment'),('objet','Objet'),
        ('animal','Animal'),('personne','Personne'),('autre','Autre')],
        string = "Qu'est-ce qui a été endommagé?" , default='batiment'
    )
    #si vehicule affiche type_vehicule
    type_batiment = fields.Selection([('immeuble','Immeuble locatif'),
        ('maison','Maison individuelle'),('hotel','Hôtel'),
       ('autre','Autre')],
        string = "De quel type de bâtiment s'agit-il?" , default='hotel'
    )
    type_objet = fields.Selection([('telephone','Téléphone mobile/tablette'),
        ('televiseur','Téleviseur'),('ordinateur','Ordinateur/ ordinateur portable'),
       ('autre','Autre')],
        string = "Quel type d'objet a été endommagé?" , default='telephone'
    )
    type_animal = fields.Selection([('chien','Chien'),
        ('chat','Chat'),('cheval','Cheval'),
       ('autre','Autre')],
        string = "De quel type d'animal' s'agit-il?" , default='chien'
    )
    etat_animal = fields.Selection([('blesse','Blessé'),
        ('decede','Décédé'),('pas','Je ne sais pas')], string="L'animal est ...",default = 'pas'
    )
    type_blessure = fields.Char("De quelles blessures l'animal souffre-t-il?")
    prix_dommage =fields.Selection([('500000','< 500 000CFA'),
        ('1000000','> 1000 000CFA'), ('entre','500 000 CFA et  1000 000CFA')], 
        string="A combien estimez-vous le dommage?"
    )
    
    date_approximative = fields.Boolean("il s'agit d'une date approximative")
   

    state = fields.Selection([('cours','En cours'),
        ('traite','Traitée'),('rejete','Rejetée')],
        default='cours'
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

   
    def action_traite(self):
        for rec in self:
            rec.state = 'traite'

    def action_retour(self):
        for rec in self:
            rec.state = 'cours'
    
    def action_rejete(self):
        for rec in self:
            rec.state = 'rejete'