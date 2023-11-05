from odoo import models, fields, api

class UniversitySalle(models.Model):

    _name = 'university.salle'
    _rec_name = 'lib'

    lib = fields.Text(string='lib')
    capacite = fields.Text(string='capacite')

    # matiere_id
    matiere_ids = fields.One2many('university.matiere', 'sale_id')





