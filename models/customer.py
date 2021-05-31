# https://www.odoo.com/documentation/14.0/howtos/backend.html

from odoo import models, fields, api, _


class Customer(models.Model):
    _inherit = "res.partner"

    pets_ids = fields.One2many('pets', 'partner_id', string='Pets')
    appointment_ids = fields.One2many('calendar.event', 'pet_owner_id', string='Appointment')
    appointment_count = fields.Integer(string="Count Sale Order", default=0, compute='count_appointment')
    phone = fields.Char(string='Telephone')
    #type = fields.Selection([ ('', ''),('contact', 'Contact'),('invoice', 'Invoice Address'),('delivery', 'Delivery Address'),('other', 'Other Address'),('private', 'Private Address'),('test', 'Test'),],'Type', default='')
    type = fields.Selection([ ('', ''),],'Type', default='')

    @api.depends('pets_ids')
    def count_appointment(self):
        data = self.env['calendar.event'].search([('pet_owner_id', '=', self.id)])
        self.appointment_count = len(data)

    def view_appointment(self):
        action = {
            'name': _('Appointments'),
            'domain': [('pet_owner_id', '=', self.id)],
            'res_model': 'calendar.event',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
        return action


