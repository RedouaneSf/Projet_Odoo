from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

from odoo import models, fields, api


class UniversityEtep(models.Model):
    _name = 'university.epet'

    etudiant_id = fields.Many2one(comodel_name='university.etudiant')
    epreuve_id = fields.Many2one(comodel_name='university.epreuve')
    matiere_id = fields.Many2one(comodel_name='university.matiere')
    note = fields.Float(string='note')











