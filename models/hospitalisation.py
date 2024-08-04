# -*- coding: utf-8 -*-
# https://www.odoo.com/documentation/14.0/howtos/backend.html

from odoo import models, fields, api, _
from datetime import datetime

class Hospitalisations(models.Model):
    _name = "hospitalisations"
    _description = "hospitalisations"
    
    name = fields.Char(string="Name", required=True, default="Vaccination")
    description = fields.Text(string="Description")
    date = fields.Date(string="Hospitalization Date", default=datetime.today(), required=True, readonly=True)
    stage = fields.Selection([('Admitted', 'Admitted'), ('Discharged', 'Discharged'), ('Died', 'Died')
                             ], string="Stage", required=True)
    pet_owner_id = fields.Many2one("res.partner", string="Pet Owner", required=True, readonly=True)
    email = fields.Char(related="pet_owner_id.email", string="Email")
    mobile = fields.Char(related="pet_owner_id.mobile", string="Mobile")
    phone = fields.Char(related="pet_owner_id.phone", string="Telephone")
    pet_name_id = fields.Many2one("pets", string="Pet Name", domain="[('partner_id','=',pet_owner_id)]", required=True, readonly=True)
    type_of_animal = fields.Many2one("animal.type", related="pet_name_id.animal_type", string="Species")
    breed = fields.Many2one('breed', related="pet_name_id.breed", string="Breed")
    sex = fields.Selection([('male', 'Male'), ('female', 'Female')], related="pet_name_id.sex", string="Gender")
    birthdate = fields.Date(related="pet_name_id.birthdate", string="Birthdate", required=True)
    last_vaccination = fields.Date(related="pet_name_id.last_vaccination", string="Last Vaccination")
    hospitalisation_id = fields.Many2one("calendar.event", string="Related Appointment", readonly=True)
    
    def open_hospitalisations_form(self):
        return {
            'name': 'Open',
            'type': 'ir.actions.act_window',
            'res_model': 'hospitalisations',
            'view_id': self.env.ref('veterinary_v14.hospitalisations_form_view').id,
            'view_type': 'form',
            'view_mode': 'form',
            'context': {},
            'res_id': self.id
        }