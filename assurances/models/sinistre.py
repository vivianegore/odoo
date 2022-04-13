from odoo import fields, models

class Sinistre(models.Model):
    _name = 'assurfaz.sinistre'
    _inherit = ['mail.thread']
    _description = 'Déclaration de sinistres'
    _rec_name = 'type_client'

    
    type_client = fields.Selection([('particulier','Clients Particuliers'),
        ('entreprise','Client Entreprise')], string="Type de Clients",default = 'particulier'
    )
    type_sinistre_entreprise = fields.Selection([('automobile','Assurance automobile'),
        ('responsabilite','Responsabilité civile d’entreprise / responsabilité civile professionnelle'),
        ('technique','Assurance technique'),('chose','Assurance de choses'),
        ('autre','Autres sinistres')],
        string = "Type du sinistre", default = 'automobile'
    )
    type_sinistre_particulier = fields.Selection([
        ('voiture','Voiture'),('menage','Ménage '),
        ('responsabilite','Responsabilité civile privée / Dommage locataire'),
        ('batiment','Bâtiment '),('accident','Accident'),
        ('construction','Construction'),('moto','Moto '),('garantie','Garantie de loyer '),
        ('objet','Objets de valeur'),
        ('paiement','Protection des paiements '),('autre','Autres sinistres')],
        string = "Type du sinistre", default = 'voiture'
    )

    cause_sinistre_automobile= fields.Selection([('accident','Accident de la circulation / collision'),
        ('bris','Bris de glace'),
        ('vol','Vol / Effraction'),('incendie','Incendie, incendie électrique,foudre,explosion'),
        ('collision','Collision avec un véhicule prêté')],
        string = "Cause du sinistre" , default = 'accident'
    )

    #type_sinistre_particulier == menage
    cause_sinistre_menage  = fields.Selection([('vol','Vol, cambriolage, perte'),
        ('endommagement','Endommagement et destruction')],
        string = "Cause du sinistre" , default = 'vol'
    )
    dommage_sinistre_menage = fields.Selection([('smartphone','Smartphone/tablette'),
        ('velo','Vélo / Vélo électrique'),
        ('cambriolage','Cambriolage'),('cyber','Cyber'),
        ('autre','Autre dommage')],
        string = "De quel dommage s’agit-il?" , default = 'cambriolage'
    )
    sinistre_menage_smartphone = fields.Selection([('vole','Mon smartphone a été volé'),
        ('perdu','J\'ai perdu mon smartphone')],
        string = "Racontez-nous ce qui s’est passé..." , default = 'perdu'
    )
    sinistre_menage_velo = fields.Selection([('vole','Mon vélo a été volé'),
        ('perdu','J\'ai perdu mon vélo')],
        string = "Racontez-nous ce qui s’est passé..." , default = 'perdu'
    )
    sinistre_menage_cambriolage = fields.Selection([('vole','J\'ai été volé(e)'),
        ('perdu','J\'ai perdu quelque chose')],
        string = "Racontez-nous ce qui s’est passé..." , default = 'perdu'
    )
    autre_dommage_menage = fields.Char("Autre dommage")
    lieu_sinistre = fields.Selection([('domicie','Au domicile'),
        ('hors','Hors du domicile')], string="Lieu du sinistre? ", default = 'domicie'
    )
    #si hors description_lieu et localité apparaissent
    description_lieu = fields.Char("Veuillez décrire le lieu")
    sinistre_menage_cyber = fields.Selection([('compte','Comptes en ligne et carte de crédit'),
        ('harcelement ','Harcèlement en ligne'),('shopping','Shopping en ligne'),
        ('donnee ','Sauvetage des données, élimination des virus et assistance informatique')],
        string = "Votre dommage concerne quel domaine?" , default = 'compte'
    )
    #cause_sinistre_menage = endommagement
    destruction_sinistre_menage = fields.Selection([('smartphone','Smartphone/tablette'),
        ('loisir','Articles de sport et de loisirs'),
        ('appareil','Appareils électroniques de loisirs'),('lunette','Lunettes ou appareils auditifs'),
        ('incendie','Incendie'),('naturel','Evènement naturel'),
        ('eau','Dégats d\'eau'),
        ('dommage','Dommage causé en tant que locataire'),('bris','Bris de glace et de céramique'),
        ('autre','Autre dommage')],
        string = "De quel dommage s’agit-il?" , default = 'incendie'
    )
    parole_donne = fields.Boolean("Je donne ma parole ")
    appareil_endommage = fields.Selection([('smartphone','Smartphone'),
        ('tablette','Tablette')], string="Qu’est-ce qui a été endommagé? ", default = 'smartphone'
    )
    marque_appareil = fields.Selection([ ('apple','Apple'),('samsung','Samsung'),   
        ('huawei','Huawei'),('lg','LG'),
        ('nokia','Nokia'),('sony','Sony'),
        ('autre','Autre marque/fabricant')],
        string = "Marque" , default = 'samsung'
    )
    Type_smartphone = fields.Char("Type de smartphone")
    Type_tablette = fields.Char("Type de tablette")
    capacite_stockage = fields.Selection([ ('8','8 Go'),('16','16 Go'),   
        ('32','32 Go'),('64','64 Go'),
        ('128','128 Go'),('256','256 Go'),('512','512 Go'),('1','1 To'),
        ('inconnu','Inconnu')],
        string = "Capacité de stockage " , default = '64'
    )
    proprietaire_appareil = fields.Selection([('oui','Oui'),
        ('non','Non')], string="L’appareil appartient-il à votre employeur?",default = 'non'
    )
    #si oui
    usage_prive = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Utilisez-vous également l’appareil à titre privé?",default = 'non'
    )
    dommage_appareil = fields.Selection([('chute','Chute'),
        ('eau','Chute dans l\'eau'),
        ('ecoulement','Ecoulement/fuite de liquide'),('choc','Choc involontaire ( ex: contre le bord d\'une table)'),
        ('pression','Dommage suite à une pression/charge (ex:dans un sac à dos)'),
        ('assis','Assis/marché sur l\'appareil par inadvertance'),
        ('defaut','Défaut technique inconnu'),
        ('autre','Autre')],
        string = "Comment l’appareil a-t-il été endommagé?" , default = 'ecoulement'
    )
    detail_circonstance = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Souhaitez-vous ajouter des informations sur les circonstances du sinistre?",default = 'non'
    )
    
    statut_demandeur = fields.Selection([('abonne','un abonné de Assurfaz'),
        ('autre','Autre personne')], string="Qui êtes-vous", default = 'abbonne'
    )

    #type_sinistre_particulier == automobiles
    #demande d'information
    info = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Quelqu'un a-til été blessé?", default = 'non'
    )
    blessure_description = fields.Html("Décrivez la blessure")
    info2 = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Votre véhicule a-t-il été endommagé?",default = 'non'
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
        string="Qui conduisait le véhicule?"
    )
    accident = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Un autre véhicule a-t-il été endommagé?",default = 'non'
    )
    chose_endommage = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Des choses emportées dans votre véhicule ont-elles été endommagées?",default = 'non'
    )
    #si oui : 
    description_chose = fields.Html("Quelles choses emportées dans votre véhicule ont été endommagées?")

    #si on choisit une personne que vous ne connaissez pas 
    name_conducteur= fields.Char("Nom du conducteur")
    pname_conducteur = fields.Char("Prénom du conducteur")
    adresse_conducteur = fields.Char("Adresse du conducteur")
    email_conducteur = fields.Char("Adresse email du conducteur")
    pays_conducteur = fields.Char("Pays du conducteur")
    date_naissance = fields.Date("Date de naissance du conducteur ")
    date_permis = fields.Char("Permis de conduire délivré le ")

    #décrire le déroulement du sinistre : Vous êtes éventuellement en possession de photos relatives au dommage. Veuillez les conserver, elles pourront être utilisées par la suite.
    description_sinistre = fields.Html("Veuillez décrire le déroulement")
    pays_personne= fields.Char("Pays")
    ville_personne= fields.Char("Ville")
    # Où et quand les faits se sont-ils passés?
    date_fait = fields.Date ("Quand le sinistre s’est-il produit?")
    localite_sinistre = fields.Char("Où le sinistre s'est-il produit?")

    #Selon vous, êtes-vous responsable de l'accident?
    responsable_accident = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Selon vous, êtes-vous responsable de l'accident?",default = 'non'
    )
    dommage_declare = fields.Selection([('oui','Oui'),
        ('non','Non')], string="Le dommage a-t-il été déclaré à la police?",default = 'non'
    )
    declaration_police = fields.Html("Auprès de quel poste de police?")
    
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

    #type_sinistre_entreprise = responsabilite
    dommage_responsabilite_cause = fields.Selection([('vehicule','Véhicule endommagé'),
        ('objet','Objet endommagé'),('animal','Animaux blessés'),
        ('personne','Personnes blessées'),('fortune','Préjudice de fortune')],
        string = "Quel dommage a été causé?" , default = 'fortune'
    )
    #où est survenu le sinistre et quand? : date, localité, pays 
    pays_sinistre= fields.Char("Pays où le sinistre s'est produit")
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
    #type_sinistre_entreprise = technique
    #date, localité, pays
    #description_sinistre
    dommage_cause = fields.Html("Veuillez énumérer les dommages")
    #prix_dommage
    #dommage
    cas = fields.Char("Qui a annoncé le cas?")
    #declaration_police
    nom_agent = fields.Char("Nom de l'agent")
    #preneur, presentation
    #numero_police
    #nom, pnom,npa formule_appel,etc...

    #type_sinistre_entreprise = chose
    #même formulaire que l'assurance technique

    #type_sinistre_entreprise = autre
    #même formulaire que l'assurance technique sauf prix_dommage, nom_agent,cas


    #type_sinistre_particulier == voiture
    #même formulaire que assurance automobile du client entreprise

    #type_sinistre_particulier == batiment
    #même formulaire que l'assurance technique sauf  nom_agent,cas

    #type_sinistre_particulier == responsabilite
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
    #description_sinistre
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
    #date_fait
    #prix_dommage
    localisation_sinistre = fields.Selection([('residence','A mon adresse de résidence'),
        ('autre','A une autre adresse'),('etranger','A l\'etranger')], string="Où le sinistre s'est-il produit?",
        default = 'etranger'
    )
    # si etranger: pays apparaît
    # autre: lieu et npa apparaîssent
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
    #etat_animal
    #type_blessure_personne
    #prix_dommage
    #description_sinistre
    #date_fait
    date_approximative = fields.Boolean("il s'agit d'une date approximative")
    #localisation_sinistre
    #Lésé: coordonnées du bailleur

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
    #numéro de police
    #entreprise : nom de l'entreprise
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
    #date_naissance, npa, lieu, pays, telephone , email,,coordonnee_paiemeent
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

    #déclaration d'accident
    #date_fait
    #lieu
    #description_sinistre
    #dommage_declare
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
    medecin_traitant = fields.Char("Médécin traitant")
    #npa, lieu, pays, telephone

    #type_sinistre_particulier == construction
    #même formulaire que l'assurance technique et bâtiment sauf  nom_agent,cas

    #type_sinistre_particulier == moto
    #même formulaire que automobile 

    #type_sinistre_particulier == objet
    #même formulaire que l'assurance technique sauf  nom_agent,cas

    #type_sinistre_particulier == garantie
    #même formulaire que objet sauf  nom_agent,cas

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
    #coordonnee_paiement
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



    #type_sinistre_particulier == lunette
    #même formulaire que l'assurance technique sauf  nom_agent,cas

    #type_sinistre_particulier == bateau
    #numero_police
    type_bateau = fields.Selection([('voilier','Voilier'),('moteur','Bateau à moteur '),
        ('autre','Autres')],
        string = "De quel type de bateau s’agit-il?", default = 'moteur'
    )
    #marque, plaque_controle
    proprietaire_bateau = fields.Selection([('oui','Oui'),('non','Non ')],
        string = "Êtes-vous propriétaire du bateau assuré par ASSURFAZ?", default = 'oui'
    )
    #titre, name, pname, email,telephone
    #sinon entreprise, npa, localite, personne, telephone, email
    #où se trouve le bateau
    #adresse, localite, telephone
    #date_fait, pays
    sinistre_survenu = fields.Selection([('tempete','Tempête'),('bris','Bris de glace/vol/acte de malveillance'),
        ('collision','Collision'),('autre','Autre')],
        default = 'collision', string="Comment le sinistre est-il survenu?"
    )
    #description_sinistre
    dommage_bateau = fields.Selection([('propre','Mon propre bateau'),('tiers','Un bateau appartenant à un tiers'),
        ('autre','Autres')], default = 'tiers',
        string = "Qu’est-ce qui a subi le dommage lors de l’événement?"
    )
    partie_bateau_endommage = fields.Selection([('voile','Voile / manœuvre dormante / manœuvre courante'),('pont','Pont'),
        ('coque','Coque'),('immergee','Partie immergée'),('autre','Autres')], default = 'pont',
        string = "Quelle partie de votre bateau a été endommagée?"
    )
    dommage_bateau_autre = fields.Char("Qu’est-ce qui a été endommagé exactement?")
    #prix_dommage
    #formule_appel, civilité, name, pname, numero, npa, localite, pays, telephone, email

    
    #type_sinistre_particulier == voyage
    #même formulaire que l'assurance technique sauf  nom_agent,cas

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
