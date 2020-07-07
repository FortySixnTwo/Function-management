# -*- coding: utf-8 -*-
"""
Beginning of 'Set menu Tool'

Created on Tue Jul  7 12:14:24 2020

@author: Nathan
"""

class Element(): # Class for elements of a dish & their allergen information
    def __init__(self, Allium, Gluten, Shellfish, Eggs, Fish, Lupin, Dairy, Molluscs, Mustard, Nuts, Peanuts, Sesame, Soya, Sulphites):
        self.Allium=False
        self.Gluten=False
        self.Shellfish=False
        self.Eggs=False
        self.Fish=False
        self.Lupin=False
        self.Dairy=False
        self.Molluscs=False
        self.Mustard=False
        self.Nuts=False
        self.Peanuts=False
        self.Sesame=False
        self.Soya=False
        self.Sulphites=False


CarrotPuree=Element(Dairy=True)

print(CarrotPuree.Dairy)
