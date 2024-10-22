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
        'ctnews.assets_frontend': [
            'ctnews/static/js/vendor/*',
            'ctnews/static/js/*.js',

            'ctnews/static/scss/_color.scss',
            'ctnews/static/scss/_variables.scss',
            'ctnews/static/scss/_mixins.scss',
            'ctnews/static/scss/_overlay.scss',
            'ctnews/static/scss/_common.scss',

            'ctnews/static/scss/_headerMenu.scss',
            'ctnews/static/scss/_trending.scss',
            'ctnews/static/scss/_wecky-new.scss',
            'ctnews/static/scss/_whats-new.scss',
            'ctnews/static/scss/_wecky2-new.scss',
            'ctnews/static/scss/_youtube.scss',
            'ctnews/static/scss/_recent-articles.scss',
            'ctnews/static/scss/_about-page.scss',
            'ctnews/static/scss/_footer.scss',
            'ctnews/static/scss/_services.scss',
            'ctnews/static/scss/_blog_page.scss',
            'ctnews/static/scss/_contact.scss',
            'ctnews/static/scss/_bradcam.scss',
            'ctnews/static/scss/_extend.scss',
            'ctnews/static/scss/_elements.scss',
        ],
    },
}

