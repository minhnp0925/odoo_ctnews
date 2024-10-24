#-*- coding: utf-8 -*-
from odoo import models, fields, api
from .utils import time_ago

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

    website_url = fields.Char(string="Website URL", compute="_compute_website_url")
    @api.depends('name')
    def _compute_website_url(self):
        for category in self:
            slug = self.env['ir.http']._slug(category)
            category.website_url = "/news/%s" % slug

    @api.depends('article_ids')
    def _compute_article_count(self): # model instance is a collection of records
        for record in self:
            record.article_count = len(record.article_ids)

    # Create navbar menu
    @api.model_create_multi
    def create(self, vals):
        # Call the super method to create the category first
        category = super(Category, self).create(vals)

        # Automatically create a corresponding website menu for this category
        self._create_category_menu(category)

        return category

    def _create_category_menu(self, category):
        """Helper method to create a website navbar menu item for the given category."""
        website = self.env['website'].get_current_website()  # Get the current website

        # Create a new menu item directly in the website's navbar for this category
        self.env['website.menu'].create({
            'name': category.name,
            'url': category.website_url,
            'parent_id': False,  # No parent menu
            'website_id': website.id,
        })

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
    view_count = fields.Integer('View Count', default=0)
    active = fields.Boolean(string="Active", default=True)

    # Maps to Category
    category_id = fields.Many2one(comodel_name='ctnews.category', string='Category', required=True, ondelete='cascade',
                                  default=lambda self: self.env['ctnews.category'].search([], limit=1))
    
    # Get category name
    category_name = fields.Char(compute='_compute_category_name')
    def _compute_category_name(self):
        for record in self:
            record.category_name = record.category_id.name

    # Maps to Keyword
    keyword_ids = fields.Many2many(comodel_name='ctnews.keyword', string='Keywords in Article')

    # Time calculation
    time_ago = fields.Char(compute='_compute_time_ago')

    def _compute_time_ago(self):
        for record in self:
            record.time_ago = time_ago(record.create_date)

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




