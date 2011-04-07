#-*- coding: utf-8 -*-

from CaseTTT import *
import gtk

class PlateauTTT:
  def __init__(self, nb):
    self.cases = []
    line = []
    self.nb = nb
    i = 0
    j = 0
    while i < nb:
      while j < nb:
	line.append(CaseTTT(" "))
	j += 1
      self.cases.append(line)
      i += 1
      j = 0
      line = []
  def end(self):
    for i in range(self.nb):
      for j in range(self.nb):
	if self.cases[i][j].getValue() == " ":
	  return False
    return True
  def vainqueur(self):
    for i in range(self.nb):
      if (self.cases[0][i].getValue() == self.cases[1][i].getValue() == self.cases[2][i].getValue() != " ") or \
      (self.cases[i][0].getValue() == self.cases[i][1].getValue() == self.cases[i][2].getValue() != " " ):
	return True
    if (self.cases[0][0].getValue() == self.cases[1][1].getValue() == self.cases[2][2].getValue() != " ") or \
    (self.cases[2][0].getValue() == self.cases[1][1].getValue() == self.cases[0][2].getValue() != " "):
      return True
    return False
    
  def joue(self, line, column, case, joueurAct, joueurs):
    if self.cases[line][column].getValue() == " ":
      image = gtk.Image()
      if joueurAct == joueurs[0]:
	self.cases[line][column].setValue("X")	
	image.set_from_file("croix.jpg")
      else:
	self.cases[line][column].setValue("0")	
	image.set_from_file("rond.jpg")
      image.show()
      case.add(image)
      if self.vainqueur() == True:
	return "win"
      if self.end() == True:
	return "end"
    else :
      return "Already played"
    return "nothing"
    
	
  def affiche(self):
    affiche = ""
    i = 0
    j = 0
    k = 0
    while i < self.nb:
      while j < self.nb:
	if j == self.nb -1:
	  affiche += self.cases[i][j].getValue()
	else:
	  affiche += self.cases[i][j].getValue() + " | "
	j += 1
	k += 1
      print affiche
      affiche = ""
      i += 1
      j = 0
      
    
