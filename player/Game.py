# -*- coding: utf-8 -*-
from thePlayer import Player 
import sys
sys.path.append("\home\\anthony\\ProjetErasmus")

class Game:

	def __init__ (self):
		#self.board = Board()
		self.p1 = Player()
		self.p2 = Player()
	
if __name__ == "__main__":

	g = Game()
	print(g.p1.nom)
