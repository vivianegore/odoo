{
'name': ' Annonces immobilière',
'version' : '1.1',
'sequence': 0,
'description': 'Créer des annonces dans l\'immobilier',
'category': 'Services',
'website': 'https://www.digifaz.com',
'author': 'Viviane Gore',
'depends': ['base'],
'data': [
'security/agence_security.xml',
'security/ir.model.access.csv',
'views/agence_menu.xml',
'views/menu_type.xml',
'views/agence_property_view.xml',
'views/agence_type_view.xml',
'views/agence_tag_views.xml',
'views/agence_offer_view.xml',
],
'installable': True,
'application': True,
'auto_install': False,
'license': 'LGPL-3',
}