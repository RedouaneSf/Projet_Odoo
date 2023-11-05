from odoo import models, fields, api

class UniversityUniversite(models.Model):

    _name = 'university.universite'
    _rec_name = 'nom'

    code = fields.Text(string='code')
    nom = fields.Text(string='nom')
    adresse = fields.Text(string='adresse')
    ville = fields.Text(string='ville')
    #departement_ids
    departement_ids = fields.One2many('university.departement', 'universite_id')

