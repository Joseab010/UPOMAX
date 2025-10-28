# -*- coding: utf-8 -*-
{
    'name': "gym",

    'summary': """Gestion del modulo gym""",

    'description': """Gestion de clases, usuarios, material, etc.""",

    'author': "TSI - UPO",
    'website': "https://www.upo.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/18.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/classes_views.xml',
        'views/users_view.xml',
        'views/instructores_view.xml',
        'views/menu.xml',
        'demo/gym.users.csv', # Colocar el fichero de carga aqui siempre y cuando no hayas cargado los datos demo al instalar la BD de Odoo.
        'demo/gym.instructores.csv', # Colocar el fichero de carga aqui siempre y cuando no hayas cargado los datos demo al instalar la BD de Odoo.
        'demo/gym.classes.csv', # Colocar el fichero de carga aqui siempre y cuando no hayas cargado los datos demo al instalar la BD de Odoo.
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/gym.users.csv', # Colocar el fichero de carga aqui siempre y cuando hayas instalado los datos demo al instalar la BD de Odoo.
        #'demo/gym.instructores.csv', # Colocar el fichero de carga aqui siempre y cuando hayas instalado los datos demo al instalar la BD de Odoo.
        #'demo/gym.classes.csv' # Colocar el fichero de carga aqui siempre y cuando hayas instalado los datos demo al instalar la BD de Odoo.
    ],
    'application': True,
}
