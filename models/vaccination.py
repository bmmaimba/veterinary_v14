# -*- coding: utf-8 -*-
# https://www.odoo.com/documentation/14.0/howtos/backend.html

from odoo import models, fields, api, _
from datetime import datetime

class Vaccinations(models.Model):
    _name = "vaccinations"
    _description = "vaccinations"
    
    name = fields.Char(string="Name", default="Vaccination", required=False, readonly=True)
    description = fields.Text(string="Description")
    date = fields.Date(string="Vaccination Date", default=datetime.today(), required=True, readonly=True)
    stage = fields.Selection([('Today', 'Today'), ('Future', 'Future'), ('Done', 'Done')
                             ], string="Stage/When", required=True)
    type_of_vacc = fields.Selection([('Rabies', 'Rabies'), ('3in1', '3in1'), ('3in1Rabies', '3in1 & Rabies'), 
                                     ('5in1', '5in1'), ('5in1Rabies', '5in1 & Rabies'), ('Leukemia', 'Leukemia')
                                    ], string="Type of Vaccination", required=True, readonly=True)
    pet_owner_id = fields.Many2one("res.partner", string="Pet Owner", required=True, readonly=True)
    email = fields.Char(related="pet_owner_id.email", string="Email")
    mobile = fields.Char(related="pet_owner_id.mobile", string="Mobile")
    phone = fields.Char(related="pet_owner_id.phone", string="Telephone")
    pet_name_id = fields.Many2one("pets", string="Pet Name", domain="[('partner_id','=',pet_owner_id)]", required=True, readonly=True)
    type_of_animal = fields.Many2one("animal.type", related="pet_name_id.animal_type", string="Species")
    breed = fields.Many2one('breed', related="pet_name_id.breed", string="Breed")
    sex = fields.Selection([('male', 'Male'), ('female', 'Female')], related="pet_name_id.sex", string="Gender")
    last_vaccination = fields.Date(related="pet_name_id.last_vaccination", string="Last Vaccination")
    next_vaccination = fields.Date(string="Next Vaccination")
    appointment_id = fields.Many2one("calendar.event", string="Related Appointment", readonly=True)
   
    def open_vaccination_form(self):
        return {
            'name': 'Open',
            'type': 'ir.actions.act_window',
            'res_model': 'vaccinations',
            'view_id': self.env.ref('veterinary_v14.vaccinations_form_view').id,
            'view_type': 'form',
            'view_mode': 'form',
            'context': {},
            'res_id': self.id
        }
        
#    @api.onchange('date')
#    def _check_change(self):
#       if self.date:
#       date_1= (datetime.strptime(self.date, '%Y-%m-%d')+relativedelta(days =+ 365))
#       self.next_vaccination =date_1
#       else:
#        self.next_vaccination =False