# -*- coding: utf-8 -*-
import werkzeug
import itertools
import pytz
import babel.dates
from collections import defaultdict

from odoo import http, fields, tools, models
from odoo.addons.website.controllers.main import QueryURL
from odoo.http import request
from odoo.tools import html2plaintext
from odoo.tools.misc import get_lang
from odoo.tools import sql

class Ctnews(http.Controller):
    @http.route('/test', auth='public', website=True)
    def news_test(self, **kwargs):
        # Render the template
        return http.request.render('ctnews.news_website_homepage', {})
    
    @http.route('/news', auth='public', website=True)
    def get_latest_news(self, **kwargs):
        # Fetch the 6 newest articles
        articles = request.env['ctnews.article'].search([], order="write_date desc", limit=5)

        # Pass the articles to the template
        return request.render('ctnews.homepage', {
            'articles': articles
        })


