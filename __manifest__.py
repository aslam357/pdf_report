{
    'name': 'Academy',
    'version': '1.0',
    'summary': 'Manage teachers and students',
    'sequence': 10,
    'description': """
        Academy module to manage teachers and students.
    """,
    'category': 'Education',
    'author': 'Aslam',
    'website': 'http://www.yourwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/view.xml',
    ],
    'images': ['/home/aslam/odoo/addons/academy/static/description/logo.png'],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
