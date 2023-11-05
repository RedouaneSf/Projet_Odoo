from odoo import models, fields, api



class UniversityModule(models.Model):
    _name = 'university.module'
    _rec_name = 'intitule'

    id = fields.Text(string='code')
    intitule = fields.Text(string='intitule')
    volume_hor = fields.Integer(string='volume_hor')
    note_min = fields.Float(string='note_min')

    #matiere_id
    #matiere_ids = fields.One2many('university.matiere','module_id')

    #filiere_id

    filiere_id = fields.Many2one(comodel_name='university.filiere')

    matiere_ids = fields.Many2many('university.matiere', "mod_mat_rel",
                                                      "intitule", "lib")






