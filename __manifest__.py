# -*- coding: utf-8 -*-
############################################################################
#    Coded by: Humanytek-Team (https://github.com/humanytek-team)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Merge Mutiple Invoices',
    'summary': """Allow your users to Merge Mutiple Invoices.""",
    'description': """
        Allow your users to Merge Mutiple Invoices
        merge invoice invoices mergeing invoice mergeing merge invoices merging invoice merging invoices
    """,
    'version': '12.1.0.0',
    'category': 'Accounting',
    'author': 'Humanytek',
    'website': 'http://humanytek.com',
    'depends': [
        'account',
    ],
    'data': [
        'wizard/merge_wizard_view.xml',
    ],
    'installable': True,
    'sequence': 1,
    'price': 12,
    'currency': 'EUR',
}
