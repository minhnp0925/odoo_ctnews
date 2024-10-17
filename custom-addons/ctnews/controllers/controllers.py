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
    _articles_per_page = 12


    @http.route('/test', auth='public', website=True)
    def news_test(self, **kwargs):
        # Render the template
        return http.request.render('ctnews.news_website_homepage', {})
    
    @http.route('/news', auth='public', website=True)
    def get_latest_news(self, **kwargs):
        # Fetch the 6 newest articles
        articles = request.env['ctnews.article'].search([], order="create_date desc", limit=5)

        # Pass the articles to the template
        return request.render('ctnews.homepage', {
            'articles': articles
        })

    @http.route('/news/<model("ctnews.category"):category>', type='http', auth='public', website=True, sitemap=True)
    def get_category(self, category, page=1, key=None, **kwargs):
        """
        Return values:
        category: Category
        keywords: List[Keyword] in category
        articles_in_page: List[Article] in category
        page: current page
        total_page: total pages for pagination
        featured: List[Article] (2 featured articles)
        top_stories: List[Article] (5 highest viewcount)

        TODO: Handle tag filtering
        """

        Article = request.env['ctnews.article']
        Keyword = request.env['ctnews.keyword']

        domain = [('category_id', '=', category.id)]
        page = int(kwargs.get('page', 1))

        featured = Article.search(domain=domain, limit=2, order="create_date DESC")
        articles_in_page = Article.search(
            domain=domain, limit=self._articles_per_page, offset=2+(page-1)*self._articles_per_page, order="create_date DESC"
        )
        top_stories = Article.search(domain=domain, limit=5, order="view_count DESC")

        keywords = Keyword.search(domain=domain, order='name ASC')

        total_pages = (category.article_count - 2 + self._articles_per_page - 1) // self._articles_per_page # -2 featured articles

        values = {
            'category': category,
            'featured': featured,
            'articles_in_page': articles_in_page,
            'keywords': keywords,
            'page': page,
            'total_pages': total_pages,
            'top_stories': top_stories,
        }

        return request.render("ctnews.category_view", values)


    @http.route([
        '''/news/<model("ctnews.category"):category>/<model("ctnews.article", "[('category_id','=',category.id)]"):article>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def get_article(self, category, article, enable_editor = None, **kwargs):
        """
        Return values:
        article: Article
        most_popular: List[Article]
        category: Category

        """
        Article = request.env['ctnews.article']
        most_popular = Article.search([
            ('id', '!=', article.id),
            #('is_published', '=', True)
        ], limit=5, order='view_count DESC, create_date DESC')

        values = {
            'article': article,
            'most_popular': most_popular,
            'category': category,
            'enable_editor': enable_editor,
        }
        response = request.render("ctnews.article_view", values)

        if article.id not in request.session.get('articles_viewed', []):
            if sql.increment_fields_skiplock(article, 'view_count'):
                if not request.session.get('articles_viewed'):
                    request.session['articles_viewed'] = []
                request.session['articles_viewed'].append(article.id)
                request.session.touch()

        return response


