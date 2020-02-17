# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name' : "Convert Purchase from Sales Order",
    'version' : "13.0.0.1",
    'category' : "Purchases",
    'summary': 'This apps helps to Covert Purchase order from Sales Order',
    'description' : """
        Convert Purchase from Sales Order
        

     """,
    'author' : "Self ",
    'website'  : "",
    'depends'  : [ 'base','sale_management','purchase'],
    'data'     : [  'security/ir.model.access.csv',
                    'wizard/purchase_order_wizard_view.xml',
                    'views/inherit_sale_order_view.xml',
            ],      
    'installable' : True,
    'application' :  False,
    "images":[''],
    'live_test_url':'',
}
