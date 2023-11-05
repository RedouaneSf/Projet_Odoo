from odoo import models, fields, api

class UniversityAbsence(models.Model):

    _name = 'university.absence'
    _rec_name = 'etudiant_id'


    justifier = fields.Boolean(string='justifier')
    non_justifier = fields.Boolean(string='non_justifier')


    #etudiant_id
    etudiant_id = fields.Many2one(comodel_name='university.etudiant')

    #seance_id
    seance_id = fields.Many2one(comodel_name='university.seance')




