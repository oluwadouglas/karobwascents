{
    'name': 'karobwa_website',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Custom Website Module',
    'description': """
        Custom website module for Odoo 19
    """,
    'author': 'oluwa_douglas',
    'website': 'https://www.karobwa.com',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/website_templates.xml',
        'views/home.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'karobwa_website/static/src/css/user_theme_color_palette.css',
            'karobwa_website/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
