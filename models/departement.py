from odoo import models, fields, api, _




class UniversityDepartement(models.Model):

    _name = 'university.departement'
    _rec_name ='nom'


    nom = fields.Text(string='nom')
    #enseignant_id
    enseignant_id = fields.One2many('university.enseignant','departement_id')
    #universite_id
    universite_id = fields.Many2one(comodel_name='university.universite')
    #filiere_id
    filiere_ids = fields.One2many('university.filiere', 'departement_id')

    #comput_field
    num_ens = fields.Integer(string="number of enseignant", compute='comp_ens')

    def comp_ens(self):
     self.num_ens = len(self.enseignant_id)





