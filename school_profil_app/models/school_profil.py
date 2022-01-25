
from odoo import fields, models

class Profil(models.Model):
    _name = 'school.profil'
    _description = 'Profil des écoles'
    name = fields.Char('Nom de l\'établissement', required=True)
    #isactif = fields.Boolean('Actif?')
    email = fields.Char('Email', Required=True )
    situation_geo= fields.Char('Situation géographique', required=True)
    type= fields.Char('Type de l\'établissement')
    contact= fields.Char('Contact')
    description= fields.Text('Description') 

    