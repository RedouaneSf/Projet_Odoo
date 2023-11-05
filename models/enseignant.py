from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class UniversityEnseignant(models.Model):

    _name = 'university.enseignant'
    _rec_name = 'nom'
    _inherit = 'mail.thread'

    code = fields.Text(string='code')
    nom = fields.Text(string='nom')
    prenom = fields.Text(string='prenom')
    cin = fields.Text(string='cin')
    adresse = fields.Text(string='adresse')
    codepostal = fields.Text(string='codepostal')
    datenaissance = fields.Date(string='datenaissance')
    datedebut = fields.Date(string='datedebut')
    email = fields.Text(string='email')
    tel = fields.Text(string='tel')
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')])
    nationalite = fields.Text(string='nationalite')
    ville = fields.Text(string='ville')
    image = fields.Image(string='')

    #departement_id
    departement_id = fields.Many2one(comodel_name='university.departement')
    #matiere_id
    matiere_id = fields.Many2one(comodel_name='university.matiere')
    #mat_rel
    mat_id = fields.Many2many('university.matiere', "ens_mat_rel", "nom", "lib")

    #rel_dep
    universite_id = fields.Many2one(comodel_name='university.filiere', related='matiere_id.modules_ids.filiere_id')
    #rel_group
    group_id = fields.Many2many('university.groupe', "ens_group_rel","prenom", "nom")


    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('university.enseignant') or _('New')
        rtn = super(UniversityEnseignant, self).create(vals)
        _logger.error('M' * 50)
        _logger.error(vals)
        return rtn


