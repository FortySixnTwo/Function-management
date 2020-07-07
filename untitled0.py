# -*- coding: utf-8 -*-
"""
Beginning of 'Set menu Tool'

Created on Tue Jul  7 12:14:24 2020

@author: Nathan
"""

class Element(): # Class for elements of a dish & their allergen information
    def __init__(self,
                 Allium=bool,
                 Gluten=bool,
                 Shellfish=bool,
                 Eggs=bool,
                 Fish=bool,
                 Lupin=False,
                 Dairy=False,
                 Molluscs=False,
                 Mustard=False,
                 Nuts=False,
                 Peanuts=False,
                 Sesame=False,
                 Soya=False,
                 Sulphites=False):