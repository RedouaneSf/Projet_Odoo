# Copyright 2020 Ayouris
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'emsi_Universite',
    'description': """
        standard maroc""",
    'version': '',
    'license': 'AGPL-3',
    'author': 'Ayouris',
    'website': 'www.ayouris.com',
     'depends': ['base','mail','contacts'],

    'data': [
        'security/ir.model.access.csv',
         'data/seq_etdata.xml',
        'data/seq_ensdata.xml',
         'views/groupe.xml',
        'views/universite.xml',
        'views/departement.xml',
        'views/enseignant.xml',
        'views/filiere.xml',
        'views/module.xml',
        'views/matiere.xml',
        'views/salle.xml',
         'views/epreuve.xml',
         'views/seance.xml',
        'views/absence.xml',
        'views/etudiant.xml',
         'views/annee.xml',
         'views/epreuve_etudiant.xml',
        'views/menuitems.xml'
    ],

    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
