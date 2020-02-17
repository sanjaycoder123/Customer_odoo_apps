# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Auto Employee Creation From Users',
    'version': '12.0.0.0',
    'summary': 'This odoo App will create an active employee from the user automatically when creating a new user.',
    'category': 'HR Management',
    'description': """
        This module helps the user to create an employee in the time of creating a user or from existing users,on the user page.
    """,
    'price': 00,
    'currency': "EUR",
    'author': 'BrowseInfo',
    'website': 'http://www.browseinfo.in',
    'depends': ['base', 'hr'],
    'data': [
             "views/hr_view.xml"
             ],
	'qweb': [
		],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    "live_test_url":'https://youtu.be/T651ZPaEshk',
    "images":['static/description/Banner.png'],
}


