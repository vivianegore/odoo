from odoo import  fields, models,_


class SaleOrder(models.Model):
    _inherit = "sale.order"


    """ def action_notification_send(self):
        for rec in self:
            rec.partner_id.user_id.notify_success(message='Devis crée') """

    def action_notification_send(self):
        message = {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': _('Informations'),
                        'message': 'Devis crée',
                        'sticky': True,
                    }
        }
        for rec in self:
            if rec.user_id.partner_id: 
                return message