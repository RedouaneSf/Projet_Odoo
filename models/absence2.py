from odoo import models, fields, api

class UniversityAbsence2(models.Model):

    _name = 'university.absence2'
    _rec_name = 'lib'


    lib = fields.Text(string='libelle')
    justifier = fields.Boolean(string='justifier')
    non_justifier = fields.Boolean(string='non_justifier')

    etudiant_id = fields.Many2one(comodel_name='university.etudiant')
    matiere_id = fields.Many2one(comodel_name='university.matiere')
    seance_id = fields.Many2one(comodel_name='university.seance')

