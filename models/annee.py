from odoo import models, fields, api

class UniversityAnnee(models.Model):

    _name = 'university.annee'
    _rec_name = 'date'


    date = fields.Text(string='date')


    group_ids = fields.One2many('university.groupe', 'annee_id')