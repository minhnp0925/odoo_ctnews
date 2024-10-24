# -*- coding: utf-8 -*-
{
    'name': "ctnews",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/backend_views.xml',
        'views/frontend_homepage.xml',
        'views/frontend_article.xml',
        'views/frontend_category.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'ctnews/static/src/css/*.css',
            'ctnews/static/src/scss/_color.scss',
            'ctnews/static/src/scss/_variables.scss',
            'ctnews/static/src/scss/_mixins.scss',
            'ctnews/static/src/scss/_overlay.scss',
            'ctnews/static/src/scss/_common.scss',

            'ctnews/static/src/scss/_headerMenu.scss',
            'ctnews/static/src/scss/_trending.scss',
            'ctnews/static/src/scss/_wecky-new.scss',
            'ctnews/static/src/scss/_whats-new.scss',
            'ctnews/static/src/scss/_wecky2-new.scss',
            'ctnews/static/src/scss/_youtube.scss',
            'ctnews/static/src/scss/_recent-articles.scss',
            'ctnews/static/src/scss/_about-page.scss',
            'ctnews/static/src/scss/_footer.scss',
            'ctnews/static/src/scss/_services.scss',
            'ctnews/static/src/scss/_blog_page.scss',
            'ctnews/static/src/scss/_contact.scss',
            'ctnews/static/src/scss/_bradcam.scss',
            'ctnews/static/src/scss/_extend.scss',
            'ctnews/static/src/scss/_elements.scss',
            'ctnews/static/src/scss/_article.scss'
            
        ], 
    },
}

