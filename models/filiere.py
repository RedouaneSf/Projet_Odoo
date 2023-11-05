from odoo import models, fields, api, _

class UniversityFiliere(models.Model):

    _name = 'university.filiere'
    _rec_name = 'intitule'
    code = fields.Integer(string='code')
    intitule = fields.Text(string='intitule')
    


    #departement_id
    departement_id = fields.Many2one(comodel_name='university.departement')

    #groupe_id
    groupe_id = fields.One2many('university.groupe', 'filiere_id')

    #module_id
    module_id = fields.One2many('university.module', 'filiere_id')





