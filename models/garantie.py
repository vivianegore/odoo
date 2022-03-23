from odoo import fields, models

class Garantie(models.Model):
    _name = 'assurfaz.auto.garantie'
    _description = 'Garanties'

    garantie = fields.Selection([('pack','Packs'),('carte','A la carte')])
    garantie_list = fields.Selection([('civile','Pack Responsabilite civile(RC)'),
        ('vol','Vol'),('defence','Defence et Recours'),('incendie','Incendie'),
        ('personne','Personnes transportees'),('avance','Avance sur Recours'),('glace','Bris de glace'),
        ('complete','Tierce Complete'),('collision','Tierce Collision'),
        ('plafonnee','Tierce Plafonnee')],
        string = "Liste de garantie"
    )
    assurance_auto_id = fields.Many2one("assurfaz.auto",required = True)
    