from odoo import models, fields, api, _
#import logging
from odoo.exceptions import ValidationError

class UniversityMatiere(models.Model):

    _name = 'university.matiere'
    _rec_name = 'lib'


    lib = fields.Text(string='lib')
    coefficient = fields.Float(string='coefficient')

    #enseignant_id
    enseignant_ids = fields.One2many('university.enseignant', 'matiere_id')

    #module_id
    #module_id = fields.Many2one(comodel_name='university.filiere')

    #module_id
    sale_id = fields.Many2one(comodel_name='university.salle')

    #seance_id
    seance_ids = fields.One2many('university.seance','matiere_id')

    #epet_id = fields.One2many('university.epet','matiere_id')

    modules_ids = fields.Many2many('university.module', "mat_mod_rel","lib", "intitule")

    # ens_rel
    ens_id = fields.Many2many('university.enseignant', "mat_ens_rel", "lib", "nom")

    @api.onchange('modules_ids')
    def _onchange_modulesids(self):
        if self.modules_ids:
            #_logger.error(len(self.modules_ids.matiere_ids))
            if len(self.modules_ids.matiere_ids) >= 2:
                raise ValidationError('ERROR')

    @api.model
    def sumcoff_get(self):

        result = sum(self.coefficient)

        return result












