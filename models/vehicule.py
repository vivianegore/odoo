from odoo import fields, models

class Vehicule(models.Model):
    _name = 'assurfaz.auto.vehicule'
    _description = 'Véhicules'

   
    assurance_type= fields.Selection([('vehicule','Véhicule individuel'),
        ('flotte','Flotte automobile')],
        string= 'Vous souhaitez une assurance pour ',
        default='vehicule'
    )
    categorisation= fields.Selection([('vehicule_particulier','Véhicule particulier(VP)'),
        ('roue','2 Roues (jusqu a 4 roues max 150kgs)'),('vehicule_utilitaire',
        'Vehicule utilitaire (transport de matériels)')],
        string= 'Categorisation ',
        default='vehicule_particulier'
    )
    carburation= fields.Selection([('essence','Essence'),
        ('diesel','Diesel'),('hybride','Hybride'),
        ('electrique','Electrique')],
        string= 'Carburation ',
        default='electrique'
    )
    volumetrie_roue = fields.Selection([('50cm3','Jusqu à 50 cm3'),
        ('125cm3','Jusqu à 125 cm3'),('400cm3','Jusqu à 400 cm3'),
        ('400cm3+','plus de 400 cm3')],
        string= 'Volumetrie 2 roues ',
        default='125cm3'
    )
    option_vehicule_utilitaire = fields.Selection([('personnel','Materiel personnel'),
        ('tiers','Materiel pour tiers')],
        string= 'Options de vehicule utilitaire',
        default='personnel'
    )
    personnel_carosserie_vehicule = fields.Selection([('tourisme','Carosserie tourisme'),
        ('autre','Autre carosserie jusqu à 3,5 tonnes'),('autre+','Autre carosserie plus de 3,5 tonnes')],
        string= 'Tonnage et carosserie du vehicule ',
        default='tourisme'
    )
    tiers_carosserie_vehicule = fields.Selection([('autre','Autre carosserie jusqu à 3,5 tonnes'),
        ('autre+','Autre carosserie plus de 3,5 tonnes')],
        string= 'Tonnage et carosserie du vehicule ',
        default='autre+'
    )
    marque = fields.Selection([('suz','Suziki'),('toy','Toyota')], string= "Marque", default='suz')
    modele = fields.Selection([('mazda','Mazda'),('dacia','H23')], string= "Modele", default='mazda')
    #Détail_vehicule 
    puissance_fiscale = fields.Integer('Puissance fiscale (nombre de chevaux)') 
    date_premiere_circulation = fields.Date('Date 1ère mise en circulation')
    nombre_place = fields.Integer('Nombre de places')
    #valeur & immatriculation
    valeur = fields.Float('Valeur actuelle en CFA')
    immatriculation = fields.Char('Immatriculation')
    nombre_vehicule = fields.Integer('Nombre de vehicule')
    assurance_auto_id = fields.Many2one("assurfaz.auto",required = True)
    
    
        
      
     