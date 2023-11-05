from odoo import models, fields, api

class UniversityEpreuve(models.Model):

    _name = 'university.epreuve'
    _rec_name = 'lib'

    lib = fields.Text(string='lib')
    date = fields.Date(string='date')
    duree = fields.Integer(string='duree')


    #epet_id=enseignant_ids = fields.One2many('university.ep_et','epruve_id')








