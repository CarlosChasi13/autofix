{
    'name': "autofix",

    'summary': "Auto repair shopping managment system",

    'description': """
        System for manage: 
        -Clientes
        -Vehicles
        -Repairs
        -Mechanics
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/20.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '20.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/vehicle_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

