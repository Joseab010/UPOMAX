{
    'name': "upomax",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "UPOMAX",
    'website': "https://www.youtube.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/serie.xml',
        'views/peliculas.xml',
        'views/plataformas.xml',
        'views/franquicia.xml',
        'views/menu.xml',
        'demo/upomax.plataforma.csv',
        'demo/upomax.franquicia.csv',
        'demo/upomax.serie.csv',
        'demo/upomax.peliculas.csv'
    ],
    
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'application':True
}

