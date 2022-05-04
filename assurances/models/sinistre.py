from odoo import models

class SinistreParticulierMoto(models.Model):
    _name = 'sinistre.particulier.moto'
    _description = "Sinistre particulier moto"    

class SinistreParticulierVoiture(models.Model):
    _name = 'sinistre.particulier.voiture'
    _description = "Sinistre particulier voiture"    

class SinistreEntrepriseChose(models.Model):
    _name = 'sinistre.entreprise.chose'
    _description = "Sinistre entreprise chose"
    
class SinistreParticulierConstruction(models.Model):
    _name = 'sinistre.particulier.construction'
    _description = "Sinistre particulier construction"    

class SinistreParticulierGarantie(models.Model):
    _name = 'sinistre.particulier.garantie'
    _description = "Sinistre particulier garantie de loyer" 

class SinistreParticulierAutre(models.Model):
    _name = 'sinistre.particulier.autre'
    _description = "Sinistre particulier autre"  
   
class SinistreParticulierObjet(models.Model):
    _name = 'sinistre.particulier.objet'
    _description = "Sinistre particulier objet" 

class SinistreParticulierBatiment(models.Model):
    _name = 'sinistre.particulier.batiment'
    _description = "Sinistre particulier bâtiment" 

class Sinistre(models.Model):
    _name = 'assurfaz.sinistre'
    _description = "Sinistres"
    
