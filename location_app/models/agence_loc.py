from email.policy import default
from odoo import api, fields, models
     
class Property(models.Model):
    _name= 'agence.bureau'
    _description = 'Propriété'
    name = fields.Char('Désignation', required=True)
    description= fields.Text('Description')
    date_availability= fields.Date('Date de la disponibilité')
    expected_price=fields.Float('Prix attendu',required=True)
    selling_price= fields.Float('Prix de vente', readonly= True)
    bedrooms= fields.Integer('Nombre de chambres', default="2")
    living_area= fields.Integer('Surface en M²')
    facades= fields.Integer('Nombre de terasse')
    garage= fields.Boolean('Garage disponible?')
    garden= fields.Boolean('Jardin disponible?')
    garden_area= fields.Integer('Surface du jardin')
    last_seen = fields.Datetime("Date de création", default=lambda self: fields.Datetime.now(), readonly=True)
    garden_orientation= fields.Selection([('Nord','Orienté vers le nord'),
        ('Sud','Orienté vers le sud'),
        ('Est','Orienté vers l\'est'),
        ('Ouest','Orienté vers l\'ouest')],
        string= "Orientation du jardin",
        Required= True,
        default='Nord'
    )
    state= fields.Selection([('Nouveau','Nouvelle offre'),
        ('Offre reçue','Offre reçue'),
        ('Offre acceptée','Offre acceptée'),
        ('Offre vendue','Offre vendue'),
        ('Offre annulée','Offre annulée')],
        string= "Type d'offres",
        Required= True,
        default='Nouveau'
    )
    property_type_id= fields.Many2one("estate.property.type", string="Type de maison")
    salesman_id = fields.Many2one('res.users', string='Vendeur',default=lambda self:self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Acheteur',copy=False)
    tag_id = fields.Many2many('estate.tag', string="Tags")
    offer_ids= fields.One2many("property.offer","partner_id",string="Offres")
    total_area = fields.Float('Aire totale', compute="_compute_total_area")

    @api.depends("living_area" ,"garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    best_price = fields.Float('Meilleure offre', compute="_compute_best_price")

    @api.depends("prix")
    def _compute_best_price(self):
        for record in self:
            record.best_price = record.living_area + record.garden_area

    



class Property_type(models.Model):
    _name = 'estate.property.type'
    _description = 'Type de propriétés'
    name = fields.Char('Intitulé')
    property_type= fields.Char('Type de propriété')
   

class Property_tags(models.Model):
    _name = 'estate.tag'
    _description = 'Type de tag'
    name = fields.Char('Nom')
   
class Property_offer(models.Model):
    _name = 'property.offer'
    _description = 'Offres'
    prix = fields.Float('Prix')
    statut = fields.Selection([('Accepte','Accepté'),
        ('Refuse','Refusé')],
        string= "Statut de l\'offre",
        copy= False,
    )
    partner_id = fields.Many2one("res.partner", string="Partenaires", required=True)
    property_id = fields.Many2one('estate.property', required=True)

