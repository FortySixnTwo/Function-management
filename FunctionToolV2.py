#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Beginning of 'Set menu Tool'

Created on Tue Jul  7 12:14:24 2020

@author: Nathan
"""

class Element(): 
    """
    Class for elements of a dish & their allergen information. Also contains whether the element is vegetarian, vegan, or pescitarian.
    """
    def __init__(self, allergens=None, veg=False, vegan=False, pesci=False):
    	"""
    	Initialiser. Allows to pass a list of allergens, and bools of whether
    	the element is vegetarian, vegan, or pescitarian.
    	"""
    	self.allergens = allergens
    	self.veg=veg
    	self.vegan=vegan
    	self.pesci=pesci

    def allergen_info(self):
    	"""
    	Method which returns the list of allergens in the Element object.
    	"""
    	if self.allergens:
    		print("This element contains the following allergens: {}.".format(self.allergens))
    	else:
    		print("This element contains none of the main 13 allergens.")

    def animalProducts(self):
   		"""
   		Method which returns which animal product-based diet the element follows.
   		"""
   		if self.vegan:
   			print("This element is vegan.")
   		elif self.veg:
   			print("This element is vegetarian.")
   		elif self.pesci:
   			print("This element is pescitarian.")
   		else:
   			print("This element is not suitable for vegans, vegetarians or pescitarians.")

class Dish():
	"""
	A class which details a complete dish, with several elements.
	"""
	def __init__(self, elements):
		"""
		Initialiser method. A list of Element objects must be passed.
		"""
		self.elements = elements
		self.allergens = []
		self.veg = True
		self.vegan = True
		self.pesci = True
		for i in self.elements:
			if not i.veg:
				self.veg = False
			if not i.vegan:
				self.vegan = False
			if not i.pesci:
				self.pesci = False
			if i.allergens:
				for j in i.allergens:
					if not j in self.allergens:
						self.allergens.append(j)
		if self.allergens == []:
			self.allergens = None

	def allergen_info(self):
		"""
		Method which prints a list of allergens in the dish.
		"""
		if self.allergens:
			print("This dish contains the following allergens: {}.".format(self.allergens))
		else:
			print("This dish contains none of the 13 main allergens.")
            
	def animalProducts(self):
		"""
   		Method which returns which animal product-based diet the dish follows.
   		"""
		if self.vegan:
			print("This dish is vegan.")
		elif self.veg:
			print("This dish is vegetarian.")
		elif self.pesci:
			print("This dish is pescitarian.")
		else:
   			print("This dish is not suitable for vegans, vegetarians or pescitarians.")


"""
Everything below here is testing stuff.
"""
flour = Element(["gluten"], True, True, True)
salmon = Element(["fish"], pesci=True)
lemon = Element(veg=True, vegan=True, pesci=True)

ThickLemonyFish = Dish([flour, salmon, lemon])
ThickLemonyFish.allergen_info()
ThickLemonyFish.animalProducts()

