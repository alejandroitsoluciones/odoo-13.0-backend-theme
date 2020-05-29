# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Backend Theme V13",
    "summary": "Backend Theme V13",
    "version": "13.0.0.1",
    "category": "Theme/Backend",
	"description": """
		Backend theme for Odoo 13.0 Community Edition.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "OCA",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'ow_web_responsive',

    ],
    "data": [
        'views/assets.xml',
		'views/res_company_view.xml',
		#'views/users.xml',
        #'views/sidebar.xml',
    ],
}

