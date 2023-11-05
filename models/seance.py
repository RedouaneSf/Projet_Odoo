from odoo import models, fields, api

class UniversitySeance(models.Model):

    _name = 'university.seance'
    _rec_name = 'date'


    heure_debut = fields.Float(string='heure_debut')
    heure_fin = fields.Float(string='heure_fin')
    date = fields.Date(string='date ')

    # module_id
    matiere_id = fields.Many2one(comodel_name='university.matiere')

    #absence_id
    absence_id = fields.One2many('university.absence','seance_id')






