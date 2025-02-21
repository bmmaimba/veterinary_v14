# -*- coding: utf-8 -*-
# https://www.odoo.com/documentation/14.0/howtos/backend.html

from odoo import models, fields, api, _
from datetime import datetime

from urllib.request import Request
from urllib.request import urlopen

#import urllib.request
#import urllib
#import urllib2
#import json
#import urllib.request
#import urllib.parse
#from urllib import urllib


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    name = fields.Char(string="Appointment Name", required=False, readonly=True )
    stage_id = fields.Many2one('appointment.stages', group_expand="_read_group_stage_ids", string="Stage")
    kanban_state = fields.Selection([('inprogress', 'In Progress'), ('done', 'Ready'), ('blocked', 'Blocked')], string="Kanban State")
    pet_owner_id = fields.Many2one("res.partner", string="Pet Owner", required=True)
    pet_name_id = fields.Many2one("pets", string="Pet Name", domain="[('partner_id','=',pet_owner_id)]", required=True)
    email = fields.Char(related="pet_owner_id.email", string="Email")
    phone = fields.Char(related="pet_owner_id.phone", string="Telephone")
    mobile = fields.Char(related="pet_owner_id.mobile", string="Mobile")
    ailment = fields.Char(string="Ailment")
    type_of_animal = fields.Many2one("animal.type", related="pet_name_id.animal_type", string="Species")
    breed = fields.Many2one('breed', related="pet_name_id.breed", string="Breed")
    birthdate = fields.Date(related="pet_name_id.birthdate", string="Birthdate")
    sex = fields.Selection([('male', 'Male'), ('female', 'Female')], related="pet_name_id.sex", string="Gender")
    last_vaccination = fields.Date(related="pet_name_id.last_vaccination", string="Last Vaccination")
    tag_ids = fields.Many2many("patient.tag", related="pet_name_id.tag_ids", string="Pet Tag")
    partner_category_id = fields.Many2many("res.partner.category", related="pet_owner_id.category_id", string="Owner Tag")
    start_date = fields.Date(string="Date", default=datetime.today())
    start_time = fields.Selection([('0700', '07:00'), ('0715', '07:15'), ('0730', '07:30'), ('0745', '07:45'),
                                   ('0800', '08:00'), ('0815', '08:15'), ('0830', '08:30'), ('0845', '08:45'),
                                   ('0900', '09:00'), ('0915', '09:15'), ('0930', '09:30'), ('0945', '09:45'),
                                   ('1000', '10:00'), ('1015', '10:15'), ('1030', '10:30'), ('1045', '10:45'),
                                   ('1100', '11:00'), ('1115', '11:15'), ('1130', '11:30'), ('1145', '11:45'),
                                   ('1200', '12:00'), ('1215', '12:15'), ('1230', '12:30'), ('1245', '12:45'),
                                   ('1300', '13:00'), ('1315', '13:15'), ('1330', '13:30'), ('1345', '13:45'),
                                   ('1400', '14:00'), ('1415', '14:15'), ('1430', '14:30'), ('1445', '14:45'),
                                   ('1500', '15:00'), ('1515', '15:15'), ('1530', '15:30'), ('1545', '15:45'),
                                   ('1600', '16:00'), ('1615', '16:15'), ('1630', '16:30'), ('1645', '16:45'),
                                   ('1700', '17:00'), ('1715', '17:15'), ('1730', '17:30'), ('1745', '17:45'),
                                   ('1800', '18:00'), ('1815', '18:15'), ('1830', '18:30'), ('1845', '18:45'),
                                   ('1900', '19:00'), ('1915', '19:15'), ('1930', '19:30'), ('1945', '19:45'),
                                   ('2000', '20:00'), ('2015', '20:15'), ('2030', '20:30'), ('2045', '20:45'),
                                   ('2100', '21:00'), ('2115', '21:15'), ('2130', '21:30'), ('2145', '21:45'),
                                   ('2200', '22:00'),
                                   ], string="Time", default='0700')
    patient_id = fields.Many2one("pets")
    bill_ids = fields.One2many('sale.order', 'appointment_id', string='Bills')
    invoice_ids = fields.One2many('account.move', 'appointment_id', string='Invoice')
    prescription_ids = fields.One2many('prescription', 'appointment_id', string='Prescription')
    sale_order_count = fields.Integer(string="Count Sale Order", default=0, compute='count_sale_order')
    invoice_count = fields.Float(string="Invoice Count", default=0.0, compute='count_invoice_total')
    prescriptions_count = fields.Integer(string="Count Prescription", default=0, compute='count_prescriptions')
    today_date = fields.Datetime(default=datetime.now())

    temprature = fields.Selection([('normal', 'Normal'), ('high', 'High'), ('low', 'Low')], string="Temprature")
    pulse = fields.Selection([('normal', 'Normal'), ('high', 'High'), ('low', 'Low')], string="Pulse")
    respiration = fields.Selection([('normal', 'Normal'), ('high', 'High'), ('low', 'Low')], string="Respiration")
    weight = fields.Float(string="Weight (Kg)", default=0.00)
    muscular_skeletal = fields.Text(string="Muscular / Skeletal")
    abdominal = fields.Text(string="Abdominal")
    diagnosis = fields.Text(string="Diagnosis")
    physical_exam = fields.Text(string="Physical Exam")
    vaccination = fields.Text(string="Vaccination")
    treatments = fields.Text(string="Treatments")
    bloodtest = fields.Char(string="Blood Test")
    cpvtest = fields.Char(string="CPV Test")
    glucose = fields.Char(string="Glucose")
    skinscraping = fields.Char(string="Skin Scraping")
    c_s = fields.Char(string="C&S")
    flourescine = fields.Char(string="Flourescine")
    schirmertest = fields.Char(string="Schirmer Test")
    urinalysis = fields.Char(string="Urinalysis")
    dipstick = fields.Char(string="Dipstick")
    dipstick_cathete = fields.Char(string="Dipstick + Cathete")
    Other = fields.Char("Other")
    Other1 = fields.Text("Other")
    skin = fields.Text("Skin")
    surgical_procedure = fields.Text(string="Surgical Procedure")
    hospital_plan = fields.Text(string="Hospital Plan")
    plan = fields.Selection([('admit', 'Admit to Hospital'), ('home_with_meds', 'Home With Meds'),
                             ('observe_at_home', 'Observe at Home'), ('revisit_tomorrow', 'Revisit Tomorrow'),
                             ('revisit_3_days', 'Revisit 3 Days'), ('revisit_5_days', 'Revisit 5 Days'),
                             ('revisit_10_days', 'Revisit 10 Days'), ('return_for_bandage_change', 'Return for Bandage Change'),
                             ], string="Consult Plan")
    hospital_treatment = fields.Text(string="Hospital Treatment")
    hospital_record = fields.Text(string="Hospital Record")
    history = fields.Text(string="History")
    laboratory = fields.Text(string="Laboratory")
    xray = fields.Binary(string="X-Ray")
    ultrasound = fields.Binary(string="Ultrasound")
    pathology = fields.Binary(string="Pathology")
    bloods = fields.Binary(string="Bloods")
    reason_for_admission = fields.Text(string="Reason for Admission")
    #assignted_to = fields.Many2one("res.users", string="Assigned To")

    appointment_type = fields.Selection([('Vaccination', 'Vaccination'), ('Hospitalization', 'Hospitalization'),
                             ('Other', 'Other')
                             ], string="Appointment Type", required=True)
    type_of_vacc = fields.Selection([('Rabies', 'Rabies'), ('3in1', '3in1'), ('3in1Rabies', '3in1 & Rabies'),
                                     ('5in1', '5in1'), ('5in1Rabies', '5in1 & Rabies'), ('Leukemia', 'Leukemia')
                                    ], string="Type of Vaccination")
    vacc_date = fields.Date(string="Vaccination Date", default=datetime.today())
    vaccination_id = fields.Many2one("vaccinations", string="Vaccination Record", readonly=True)

    hospitalisation_id = fields.Many2one("hospitalisations", string="Hospitalisations Record", readonly=True)

    def open_vet_form(self):
        return {
            'name': 'Open',
            'type': 'ir.actions.act_window',
            'res_model': 'calendar.event',
            'view_id': self.env.ref('calendar.view_calendar_event_form').id,
            'view_type': 'form',
            'view_mode': 'form',
            'context': {},
            'res_id': self.id
        }

    @api.onchange('pet_owner_id')
    def onchange_pet_owner_id(self):
        if self.pet_owner_id:
            self.partner_ids = [(6,0, [self.env.user.partner_id.id, self.pet_owner_id.id])]
            #self.pet_owner_id = self.pet_owner_id.id

    #@api.model
    #def create(self, vals):
        #if vals.get('pet_owner_id') and vals.get('pet_name_id') and vals.get('today_date'):
            #pet_owner_id = self.env['res.partner'].browse(vals.get('pet_owner_id'))
            #pet_name_id = self.env['pets'].browse(vals.get('pet_name_id'))
        #vals['name'] = "Appointment-" + pet_owner_id.name + "-" + pet_name_id.name + "-" + vals.get('today_date')
        #res = super(CalendarEvent, self).create(vals)
        #return res

    @api.depends('pet_owner_id', 'prescriptions_count')
    def count_sale_order(self):
        count_sale_order = self.env['sale.order'].search([('appointment_id', '=', self.id)])
        self.sale_order_count = len(count_sale_order)

    @api.depends('pet_owner_id', 'prescriptions_count')
    def count_invoice_total(self):
        count_invoice = self.env['account.move'].search([('appointment_id', '=', self.id)])
        count = 0.0
        for total in count_invoice:
            count += total.amount_total_signed
        self.invoice_count += count

    @api.depends('pet_owner_id', 'prescriptions_count')
    def count_prescriptions(self):
        count_prescriptions = self.env['prescription'].search([('appointment_id', '=', self.id)])
        self.prescriptions_count = len(count_prescriptions)

    @api.model
    def _get_public_fields(self):
        return self._get_recurrent_fields() | self._get_time_fields() | {
            'id', 'active', 'allday',
            'duration', 'user_id', 'interval',
            'count', 'rrule', 'recurrence_id', 'show_as', 'stage_id'}

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['appointment.stages'].search([])
        return stage_ids

    def view_sale(self):
        action = {
            'name': _('View Sale'),
            'domain': [('appointment_id', '=', self.id)],
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
        return action

    # def view_invoice(self):
    #     context = {}
    #     context.update(create=True)
    #     action = {
    #         'name': _('View Invoice'),
    #         'domain': [('appointment_id', '=', self.id)],
    #         'context': context,
    #         'view_mode': 'tree,form',
    #         'res_model': 'account.move',
    #         'type': 'ir.actions.act_window',
    #     }
    #     return action

    def view_invoice(self):
        context = {
            'default_move_type': 'out_invoice',
            'default_partner_id': self.pet_owner_id.id,
            'default_appointment_id': self.id,
            #'default_payment_reference': self.name,
            'default_ref': self.name,
            'default_invoice_date': self.create_date,
            'default_invoice_date_due': self.create_date,
            'default_journal_id': self.env['account.journal'].search([('type', '=', 'Cash')], limit=1).id,
            'default_invoice_payment_term_id': self.env['account.payment.term'].search([('name','=','Immediate Payment')]).id,
            # 'default_auto_post': True,
        }
        context.update(create=True)
        action = self.env.ref('account.action_move_out_invoice_type').read()[0]
        action.update({
            'type': 'ir.actions.act_window',
            'name': _('View Invoice'),
            'res_model': 'account.move',
            'domain': [('move_type', '=', 'out_invoice'),('appointment_id', '=', self.id)],
            'context': context,
            'view_id': self.env.ref('account.view_out_invoice_tree').id,
            'search_view_id': self.env.ref('account.view_account_invoice_filter').id,
            'view_mode': 'tree,kanban,form',
        })
        return action

    def view_prescription(self):
        action = {
            'name': _('View Prescription'),
            'domain': [('appointment_id', '=', self.id)],
            'res_model': 'prescription',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
        return action

    def write(self, vals):
        if vals.get('pet_owner_id'):
            owner_id = self.env['res.partner'].browse(vals.get('pet_owner_id'))
            self.name = "Appointment-" + owner_id.name + "-" + self.pet_name_id.name + "-" + str(self.today_date)
        if vals.get('pet_name_id'):
            pet_name_id = self.env['pets'].browse(vals.get('pet_name_id'))
            self.name = "Appointment-" + self.pet_owner_id.name + "-" + pet_name_id.name + "-" + str(self.today_date)
        if vals.get('pet_name_id') and vals.get('pet_owner_id'):
            owner_id = self.env['res.partner'].browse(vals.get('pet_owner_id'))
            pet_name_id = self.env['pets'].browse(vals.get('pet_name_id'))
            self.name = "Appointment-" + owner_id.name + "-" + pet_name_id.name + "-" + str(self.today_date)
        return super(CalendarEvent, self).write(vals)

    @api.model
    def default_get(self, fields):
        fields.append('pet_owner_id')
        return super(CalendarEvent, self).default_get(fields)

class ContactTags(models.Model):
    _inherit = "res.partner.category"

    color_indicator = fields.Char(string="Indicator")
    color_def = fields.Selection([('Red1', 'Red1'), ('Orange2', 'Orange2'), ('Yellow3', 'Yellow3'), ('LightBlue4', 'Light Blue4'),
                                  ('DarkPurple5', 'Dark Purple5'), ('SalmonPink6', 'Salmon Pink6'), ('MediumBlue7', 'Medium Blue7'),
                                  ('DarkBlue8', 'Dark Blue8'), ('Fushia9', 'Fushia9'), ('Green10', 'Green10'), ('Purple11', 'Purple11'),
                                 ], string="Color Def")

class AppointmentStages(models.Model):
    _name = "appointment.stages"
    _description = "appointment.stages"

    name = fields.Char(string="Name")
    requirements = fields.Char()


class Prescription(models.Model):
    _name = "prescription"
    _description = "prescription"

    name = fields.Char(string="Prescription")
    partner_id = fields.Many2one("res.partner", string="Customer")
    appointment_id = fields.Many2one("calendar.event", string="Appointment")
    date = fields.Date(string="Date")
    prescription_tags = fields.Many2many("prescription.tag", string="Tags")
    notes = fields.Text(string="Notes")
    user_id = fields.Many2one("res.users", default=lambda self: self.env.user.id)

    @api.model
    def default_get(self, fields):
        rec = super(Prescription, self).default_get(fields)
        appointment = self.env['calendar.event'].browse(self.env.context.get('active_id'))
        if self.appointment_id not in rec:
            rec.update({
                'partner_id': appointment.pet_owner_id,
                'appointment_id': appointment.id,
            })
        return rec


class Pets(models.Model):
    _name = "pets"
    _description = "pets"

    name = fields.Char(string="Name")
    image = fields.Binary(string="Image")
    partner_id = fields.Many2one("res.partner", string="Owner")
    tag_ids = fields.Many2many("patient.tag", string="Tag")
    birthdate = fields.Date(string="Birthdate")
    animal_type = fields.Many2one("animal.type", string="Species")
    breed = fields.Many2one('breed', string="Breed")
    sex = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    description = fields.Text("Description")
    last_vaccination = fields.Date(string="Last Vaccination")
    appointment_ids = fields.One2many("calendar.event", "pet_name_id", string="Appointments")
    vaccination_ids = fields.One2many("vaccinations", "pet_name_id", string="Vaccinations")
    hospitalization_ids = fields.One2many("hospitalisations", "pet_name_id", string="Hospitalizations")

    @api.model
    def default_get(self, fields):
        fields.append('partner_id')
        return super(Pets, self).default_get(fields)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    appointment_id = fields.Many2one('calendar.event', string='Appointment')
    invoice_ids = fields.One2many('account.move', 'bill_id', string='Invoices')

    @api.model
    def default_get(self, fields):
        rec = super(SaleOrder, self).default_get(fields)
        appointment = self.env['calendar.event'].browse(self.env.context.get('active_id'))
        if self.partner_id not in rec:
            rec.update({
                'partner_id': appointment.pet_owner_id,
                'appointment_id': appointment.id,
            })
        return rec


class AccountMove(models.Model):
    _inherit = "account.move"

    appointment_id = fields.Many2one('calendar.event', string='Appointment')
    bill_id = fields.Many2one('sale.order', string='Bill')
    def write(self, vals):
        res = super(AccountMove, self).write(vals)
        for record in self:
            if record.state == 'posted' and not record.payment_reference:
                record.payment_reference = record.name
        return res


#    @api.model
#    def default_get(self, fields):
#        rec = super(AccountMove, self).default_get(fields)
#        appointment = self.env['calendar.event'].browse(self.env.context.get('active_id'))
#        if self.appointment_id not in rec:
#            rec.update({
#                'appointment_id': appointment.id,
#            })
#        return rec

# class InvoiceTransfer(models.Model):
#     _inherit = "stock.picking"
#
#     @api.model
#     def create(self, vals):
#         res = super(InvoiceTransfer, self).create(vals)
#         for record in res:
#             if record.picking_type_id.code == 'outgoing':
#                 record.action_confirm()
#                 record.action_assign()
#                 if record.state == 'assigned':
#                     immediate_transfer_line_ids = [
#                         (0, 0, {'to_immediate': True, 'picking_id': record.id})
#                     ]
#                     pick_ids = [[6,0, [record.id]]]
#                     data_id = self.env['stock.immediate.transfer'].create({'show_transfers':True, 'pick_ids':pick_ids,
#                                                                  'immediate_transfer_line_ids':immediate_transfer_line_ids})
#                     data_id.process()
#         return res