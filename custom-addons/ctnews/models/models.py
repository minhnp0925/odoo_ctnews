#-*- coding: utf-8 -*-
from odoo import models, fields, api
import odoo.addons.http_routing.models.ir_http as ir_http
from unidecode import unidecode_expect_nonascii

class Category(models.Model):
    _name = 'ctnews.category'
    _description = 'Category'
    _inherit = [
        'website.seo.metadata',
        'website.searchable.mixin',
    ]
    _order = 'name'
    _log_access = False

    name = fields.Char(string='Category Name', required=True)
    desc = fields.Char(string='Category Description')
    active = fields.Boolean(string='Active', default=True)

    # Maps to articles
    article_ids = fields.One2many(comodel_name='ctnews.article', inverse_name='category_id', string='Articles in Category')
    article_count = fields.Integer('Article Count', compute='_compute_article_count')
    @api.depends('article_ids')
    def _compute_article_count(self): # model instance is a collection of records
        for record in self:
            record.article_count = len(record.article_ids)

    # Maps to keywords
    keyword_ids = fields.One2many(comodel_name='ctnews.keyword', inverse_name='category_id', string='Keywords in Category')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Category name already exists!')
    ]

class Article(models.Model):
    _name = 'ctnews.article'
    _description = 'Article'
    _inherit = [
        'website.seo.metadata',
        'website.searchable.mixin',
        'website.published.mixin',
    ]
    _order = 'id DESC'

    def _compute_website_url(self):
        super(Article, self)._compute_website_url()
        for article in self:
            category_slug = self.env['ir.http']._slug(article.category_id)
            article_slug = self.env['ir.http']._slug(article)
            # Generate the website URL
            article.website_url = "/news/%s/%s" % (category_slug, article_slug)


    name = fields.Char(string='Title', required=True)
    abstract = fields.Char(string='Abstract')
    content = fields.Html('Content', sanitize=False)
    views = fields.Integer('View Count', default=0)
    active = fields.Boolean(string="Active", default=True)

    # Maps to Category
    category_id = fields.Many2one(comodel_name='ctnews.category', string='Category', required=True, ondelete='cascade',
                                  default=lambda self: self.env['ctnews.category'].search([], limit=1))

    # Maps to Keyword
    keyword_ids = fields.Many2many(comodel_name='ctnews.keyword', string='Keywords in Article')

class Keyword(models.Model):
    _name = 'ctnews.keyword'
    _description = 'Keyword'
    _order = 'name'
    _inherit = ['website.seo.metadata']
    _log_access = False

    
    name = fields.Char(string = 'Keyword', required = True)

    # Map to Category: Every Keyword must belong in a Category. Delete a category will delete all its tags.
    category_id = fields.Many2one(comodel_name='ctnews.category', string='Category', required=True, ondelete='cascade',
                                  default=lambda self: self.env['ctnews.category'].search([], limit=1))

    article_ids = fields.Many2many(comodel_name='ctnews.article', string='Articles with Keyword')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Keyword already exists!')
    ]




