from odoo import models, fields, api

class UniversityNote(models.Model):

    _name = 'university.note'
    _rec_name = 'note'

    note = fields.Float(string='Note')

    #epet_id = fields.One2many('university.epet','note_id')

