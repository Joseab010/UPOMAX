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
        'reports/peliculas_report.xml',
        'reports/reports.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/serie.xml',
        'views/pelicula.xml',
        'views/plataforma.xml',
        'views/franquicia.xml',
        'views/temporada.xml',
        'views/genero.xml',
        'views/productora.xml',
        'views/banda_sonora.xml',
        'views/capitulo.xml',
        'views/track.xml',
        'views/persona.xml',
        'views/review.xml',
        'views/usuario.xml',
        'views/premio.xml',
        'views/menu.xml',
        
        'demo/upomax.genero.csv',
        'demo/upomax.plataforma.csv',
        'demo/upomax.franquicia.csv',
        'demo/upomax.serie.csv',
        'demo/upomax.productora.csv',
        'demo/upomax.temporada.csv',
        'demo/upomax.capitulo.csv',
        'demo/upomax.track.csv',
        'demo/upomax.banda.sonora.csv',
        'demo/upomax.pelicula.csv',
        'demo/upomax.persona.csv',
        'demo/upomax.premio.csv',
        'demo/upomax.usuario.csv',
        'demo/upomax.review.csv',
        
    ],
    
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    
    
}

