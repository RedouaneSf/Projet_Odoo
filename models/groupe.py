from odoo import models, fields, api, _
from odoo.exceptions import ValidationError




class UniversityClassroom(models.Model):

    _name = 'university.groupe'
    _rec_name = 'nom'
    _inherit = 'mail.thread'


    id = fields.Text(string='id')
    nom = fields.Char(string='nom')
    #filiere_id
    filiere_id = fields.Many2one(comodel_name='university.filiere')
    #etudiant_id
    etudiant_ids = fields.One2many('university.etudiant', 'groupe_id')

    annee_id = fields.Many2one(comodel_name='university.annee')

    #rel
    ens_id = fields.Many2many('university.enseignant',"ens_group_rel", "nom", "prenom")
   #compute_field
    num_stu = fields.Integer(string="number of student", compute='comp_stu')
    #compute_enseigant
    num_ens = fields.Integer(string="number of enseignant", compute='comp_ens')

    def comp_stu(self):
        for record in self:
            record.num_stu = self.env['university.etudiant'].search_count(
                [('groupe_id', 'in', self.ids)])

    @api.onchange('etudiant_ids')
    def check_numberofstudents(self):
        if len(self.etudiant_ids) >4:
            #return {'warning': {'title': 'warning', 'message': 'the number of students must be less then 4'}}
            raise ValidationError('the number of students must be less then 4')


    def action_view(self):
       action = self.env.ref('projet_emsi.action_university_etudiant').read()[0]
       action['domain'] = [('groupe_id', 'in', self.ids)]
       return action

    ###################################################################


















