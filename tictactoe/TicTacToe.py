#-*- coding: utf-8 -*-
from ViewTTT import *
from PlateauTTT import *
    

    

    
def run(box):
	joueur = [1,2]
	vue = ViewTTT(PlateauTTT(3), joueur , box)
	vue.boucle()
