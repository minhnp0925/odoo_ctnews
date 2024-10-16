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

from .utils import time_ago

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

    @http.route([
        '''/news/<model("ctnews.category"):category>/<model("ctnews.article", "[('article_id','=',article.id)]"):article>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def get_article(self, category, article, enable_editor = None, **kwargs):
        """
        Return values:
        article: Article
        most_popular: List[Article]
        category: 

        """
        Article = request.env['ctnews.article']
        most_popular = Article.search([
            ('id', '!=', article.id),
            ('is_published', '=', True)
        ], limit=5, order='view_count DESC')

        for pop_article in most_popular:
            pop_article.time_ago = time_ago(pop_article.create_date)

        values = {
            'article': article,
            'most_popular': most_popular,
            'category': category,
            'enable_editor': enable_editor,
        }
        response = request.render("ctnews.article_view", values)

        if article.id not in request.session.get('articles_viewed', []):
            if sql.increment_fields_skiplock(article, 'visits'):
                if not request.session.get('articles_viewed'):
                    request.session['articles_viewed'] = []
                request.session['articles_viewed'].append(article.id)
                request.session.touch()

        return response


