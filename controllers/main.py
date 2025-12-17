# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class KarobwaWebsiteController(http.Controller):
    
    # ==================== CUSTOM CODE PAGES ====================
    # These pages use custom code and are NOT editable via website builder
    
    @http.route('/karobwa_scents', type='http', auth='public', website=True)
    def index(self, **kwargs):
        """Homepage with custom slider - Not editable via visual builder"""
        return request.render('karobwa_website.homepage', {
            'page_title': 'Welcome to Karobwa Scents',
        })
    
    @http.route('/', type='http', auth='public', website=True)
    def home(self, **kwargs):
        """Override default homepage with Karobwa website"""
        return request.render('karobwa_website.homepage', {
            'page_title': 'Welcome to Karobwa Scents',
        })
    
    # ==================== BUILDER-EDITABLE PAGES ====================
    # These pages use oe_structure and CAN be edited via website builder
    
    @http.route('/karobwa_scents/about', type='http', auth='public', website=True)
    def about(self, **kwargs):
        """About page - Editable via visual builder"""
        return request.render('karobwa_website.about_page', {
            'page_title': 'About Karobwa Scents',
        })
    
    @http.route('/karobwa_scents/shop', type='http', auth='public', website=True)
    def shop(self, **kwargs):
        """Shop page - Editable via visual builder"""
        return request.render('karobwa_website.shop_page', {
            'page_title': 'Shop Karobwa Products',
        })
    
    @http.route('/karobwa_scents/products', type='http', auth='public', website=True)
    def products(self, **kwargs):
        """Products catalog - Displays all products with professional layout"""
        Product = request.env['product.product']
        products = Product.search([('website_published', '=', True)])
        
        return request.render('karobwa_website.products_page', {
            'page_title': 'Our Products',
            'products': products,
        })


