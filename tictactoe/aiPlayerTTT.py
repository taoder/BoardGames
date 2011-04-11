#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BoardGames.player.thePlayer import aiPlayer





class aiPlayerTTT(aiPlayer):
	
	def __init__(self,name,color):
		self.name = name
		self.color = color
	

	def ai(self, board):
			#print "on est dans l'IA"
			print board.cases[1][1].getValue()
			#Si la case du milieu est vide on joue dedans
			if board.cases[1][1].getValue() == " " :
				#print "la case du milieu est vide"
				return 1,1
			else:
				#print "case du milieu non vide"
				#Sinon, on cherche si on peut finir la partie, si c'est le cas on gagne
				for i in range(board.nb):
					#print "on cherche victoire colonne ligne i = ", i
					if board.cases[i][0].getValue() == "O" and board.cases[i][1].getValue() == "O" and board.cases[i][2].getValue() == " ":
						return i,2
					elif board.cases[i][0].getValue() == "O" and board.cases[i][2].getValue() == "O" and board.cases[i][1].getValue() == " ":
						#print " t dans la place"
						return i,1
					elif board.cases[i][1].getValue() == "O" and board.cases[i][2].getValue() == "O" and board.cases[i][0].getValue() == " ":
						return i,0
					elif board.cases[0][i].getValue() == "O" and board.cases[1][i].getValue() == "O" and board.cases[2][i].getValue() == " ":
						return 2,i
					elif board.cases[0][i].getValue() == "O" and board.cases[2][i].getValue() == "O" and board.cases[1][i].getValue() == " ":
						return 1,i
					elif board.cases[1][i].getValue() == "O" and board.cases[2][i].getValue() == "O" and board.cases[0][i].getValue() == " ":
						return 1,i
					else : 
						pass
						#print "cas par defaut"
				#recherche en diagonale
				#print "on cherche victoire diag"
				#print " 0, 0 " , board.cases[0][0].getValue() , " 1, 1" , board.cases[1][1].getValue() , " 2, 2" , board.cases[2][2].getValue()
				if board.cases[0][0].getValue() == "O" and board.cases[1][1].getValue() == "O" and board.cases[2][2].getValue() == " ":
					print "first, deuxieme tour"
					return 2,2
				if board.cases[0][0].getValue() == "O" and board.cases[1][1].getValue() == " " and board.cases[1][1].getValue() == "O":
					return 1,1
				if board.cases[0][0].getValue() == " " and board.cases[1][1].getValue() == "O" and board.cases[0][0].getValue() == "O":
					return 0,0
				if board.cases[0][2].getValue() == "O" and board.cases[1][1].getValue() == "O" and board.cases[2][0].getValue() == " ":
					return 2,0
				if board.cases[0][2].getValue() == "O" and board.cases[1][1].getValue() == " " and board.cases[1][1].getValue() == "O":
					return 1,1
				if board.cases[0][2].getValue() == " " and board.cases[1][1].getValue() == "O" and board.cases[0][2].getValue() == "O":
					return 0,2
				#Sinon, on cherche si l'adversaire peut gagner en un coup, si c'est le cas on bloque		
				for i in range(board.nb):
					#print "on cherche a pas perdre ligne colonne"
					print board.cases[i][1], "cases 0 1 et cases 0 2 " , board.cases[i][1]
					if board.cases[i][0].getValue() == "X" and board.cases[i][1].getValue() == "X" and board.cases[i][2].getValue() == " ":
						return i,2
					elif board.cases[i][0].getValue() == "X" and board.cases[i][2].getValue() == "X" and board.cases[i][1].getValue() == " ":
						return i,1
					elif board.cases[i][1].getValue() == "X" and board.cases[i][2].getValue() == "X" and board.cases[i][0].getValue() == " ":
						#print "premier tour"
						return i,0
					elif board.cases[0][i].getValue() == "X" and board.cases[1][i].getValue() == "X" and board.cases[2][i].getValue() == " ":
						return 2,i
					elif board.cases[0][i].getValue() == "X" and board.cases[2][i].getValue() == "X" and board.cases[1][i].getValue() == " ":
						return 1,i
					elif board.cases[1][i].getValue() == "X" and board.cases[2][i].getValue() == "X" and board.cases[0][i].getValue() == " ":
						return 0,i
				#print "on cherche à pas perdre diag"
				if board.cases[0][0].getValue() == "X" and board.cases[1][1].getValue() == "X" and board.cases[2][2].getValue() == " " and board.cases[i][2].getValue() == " ":
					return 2,2
				if board.cases[0][0].getValue() == "X" and board.cases[1][1].getValue() == " " and board.cases[2][2].getValue() == "X" and board.cases[i][2].getValue() == " ":
					return 1,1
				if board.cases[0][0].getValue() == " " and board.cases[1][1].getValue() == "X" and board.cases[2][2].getValue() == "X" and board.cases[i][2].getValue() == " ":
					return 0,0
				if board.cases[0][2].getValue() == "X" and board.cases[1][1].getValue() == "X" and board.cases[2][0].getValue() == " " and board.cases[i][2].getValue() == " ":
					return 2,0
				if board.cases[0][2].getValue() == "X" and board.cases[1][1].getValue() == " " and board.cases[2][0].getValue() == "X" and board.cases[i][2].getValue() == " ":
					return 1,1
				if board.cases[0][2].getValue() == " " and board.cases[1][1].getValue() == "X" and board.cases[2][0].getValue() == "X" and board.cases[i][2].getValue() == " ":
					return 0,2
				#Sinon on met dans le premier coin libre
				#print "on cherche un coin libre"
				print board.cases[0][0]
				if board.cases[0][0].getValue() == " ":
					return 0,0
				elif board.cases[2][2].getValue() == " ":
					return 2,2
				elif board.cases[0][0].getValue() == " ":
					return 0,2	
				elif board.cases[0][0].getValue() == " ":
					return 2,0
				#Puis on cherche dans les quatres cases restantes
				#print "on cherche autre part"
				if board.cases[0][1].getValue() == " ":
					return 0,1
				elif board.cases[1][0].getValue() == " ":
					return 1,0
				elif board.cases[1][2].getValue() == " ":		
					return 1,2
				elif board.cases[2][1].getValue() == " ":
					return 2,1
