# -*- coding: utf-8 -*-
# https://www.odoo.com/documentation/14.0/howtos/backend.html

from odoo import models, fields, api


class AppointmentTags(models.Model):
    _name = "appointment.tags"
    _description = "appointment tags"

    name = fields.Char(string="Name")
    color = fields.Integer(string="Color")


class AnimalTypeTag(models.Model):
    _name = "animal.type.tag"
    _description = "animal.type.tag"

    name = fields.Char(string="Name")


class AnimalType(models.Model):
    _name = "animal.type"
    _description = "animal type"

    name = fields.Char(string="Name")
    animal_tag_ids = fields.Many2many("animal.type.tag", string="Tags")
    notes = fields.Text(string="Notes")


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "patient tags"

    name = fields.Char(string="Name")
    color = fields.Integer(string="Color")


class Breed(models.Model):
    _name = "breed"
    _description = "breed"
    name = fields.Char(string="Name")


class PrescriptionTag(models.Model):
    _name = "prescription.tag"
    _description = "prescription tags"

    name = fields.Char(string="Name")
    color = fields.Integer(string="Color")

