from odoo import fields, models

class Marque(models.Model):
    _name = 'assurfaz.auto.vehicule.modele'
    _description = 'Modèles de véhicules'
    _inherit = ['mail.thread']

    name = fields.Char(string="Modèle")
   
    marque_id= fields.Many2one('assurfaz.auto.vehicule.marque',string="Marque")
    