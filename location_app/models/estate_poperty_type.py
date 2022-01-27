from odoo import fields, models

class Property_type(models.Model):
    _name = 'estate.property.type'
    _description = 'Type de propriétés'
    name = fields.Char('Intitulé')