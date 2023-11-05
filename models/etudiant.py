from odoo import models, fields, api, _
import logging
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class UniversityEtudiant(models.Model):

    _name = 'university.etudiant'
    _rec_name = 'nom'
    _inherit = 'mail.thread'

    id = fields.Text(string='id')
    matricule = fields.Text(string='matricule')
    nom = fields.Text(string='Nom')
    prenom = fields.Text(string='Prenom')
    cin = fields.Text(string='Cin')
    cne= fields.Text(string='Cne')
    adresse = fields.Text(string='Adresse')
    codepostal = fields.Text(string='Codepostal')
    datenaissance = fields.Date(string='Datenaissance')
    dateinscription = fields.Date(string='Dateinscription')
    email = fields.Text(string='Email')
    tel = fields.Text(string='Tel')
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')])
    nationalite = fields.Text(string='Nationalité')
    ville = fields.Text(string='Ville')
    image = fields.Image(string='Image')
    #groupe_id
    groupe_id = fields.Many2one(comodel_name='university.groupe')

    #absence_id
    absence_ids = fields.One2many('university.absence', 'etudiant_id')
    #note

    epreuve_etud_ids = fields.One2many('university.epet', 'etudiant_id')
    #absence2_id
    absence2_ids = fields.One2many('university.absence2', 'etudiant_id')

    note_gen = fields.Float("calcule_note", store=True)
    ratt_gen = fields.Text("check_ratt", store=True)




    #related_filiere
    fil_id = fields.Many2one('university.filiere', related='groupe_id.filiere_id')
    #related_departement
    dep_id = fields.Many2one(comodel_name='university.departement', related='groupe_id.filiere_id.departement_id')

    def calcule_note(self):
       for rec in self:
           note = self.env['university.epet'].search([('etudiant_id', '=', self.id)])
           all_note = 0
           all_coff =0
           all_gen = 0
           for rec in note:
               all_note += rec.note * rec.matiere_id.coefficient
               all_coff += rec.matiere_id.coefficient
           if all_note != 0.0 and all_coff != 0.0:
               all_gen = all_note / all_coff
               _logger.error('111111111111111111111111111111111111111111111111111111111111111111111111111111')
               _logger.error(all_gen)
               _logger.error(all_coff)
               _logger.error(all_gen)

               self.note_gen = all_gen


    def check_ratt(self):
        result = ""
        for rec in self:
            note = self.env['university.epet'].search([('etudiant_id', '=', self.id)])
            cmp=0
            for rec in note:
                nm = rec.matiere_id.modules_ids.note_min
                note =rec.note
                if  note < nm :
                    result = result + ',' +rec.matiere_id.lib
                    cmp+=1
            if cmp>1:
                self.ratt_gen=" nombre ratt: "+str(cmp)+" :"+" liste des matiere a rattraper :"+ result





    @api.onchange('groupe_id')
    def _onchange_groupe_id(self):
        if self.groupe_id:
            _logger.error(len(self.groupe_id.etudiant_ids))
            if len(self.groupe_id.etudiant_ids) >= 4:
                raise ValidationError('ERROR')

    @api.model
    def create(self, vals):
        vals['matricule'] = self.env['ir.sequence'].next_by_code('university.etudiant') or _('New')
        rtn = super(UniversityEtudiant, self).create(vals)
        _logger.error('M' * 50)
        _logger.error(vals)
        return rtn


    @api.model
    def name_get(self):
        result = []
        for etudiant in self:
            name = etudiant.nom if etudiant.nom else '' + ' ' + etudiant.prenom if etudiant.prenom else ''
            result.append((etudiant.id, name))

        return result

    @api.onchange('epreuve_etud_ids')
    def _onchange_groupe_id(self):
        if self.epreuve_etud_ids:
            _logger.error(len(self.epreuve_etud_ids))
            _logger.error(len(self.epreuve_etud_ids) >= 4)
            if len(self.epreuve_etud_ids) > 4:
                raise ValidationError('ERROR')

