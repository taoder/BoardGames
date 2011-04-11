#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PlateauTTT import *
from BoardGames.base.Game import Game
from BoardGames.player.thePlayer import *
from aiPlayerTTT import aiPlayerTTT
import pygtk
pygtk.require('2.0')
import gtk
from PIL import ImageTk
import Tkinter as Tk
from PIL import Image

class TicTacToe(Game):
	
				
	def play(self, widget, evenement,  i, j ,fenetre):
		result = self.board.putpawn(i, j, self.joueurAct, self.player)
		if result != "Already played":
			if result == "win" or result == "end":
				self.buffer = gtk.TextBuffer(table=None)
				if result == "win":
					self.buffer.set_text("Congratulations player {0} you win".format(self.joueurAct.getName()))
				if result == "end":
					self.buffer.set_text("It's a tie")
				text = gtk.TextView(self.buffer)
				text.set_editable(False)
				bbox = gtk.VBox(True, 1)
				resultbox = gtk.HBox(True, 1)
				bquit = gtk.Button("Quit")
				bquit.connect("clicked", self.passage, fenetre,"quit")
				breplay = gtk.Button("Replay")
				breplay.connect("clicked", self.passage,fenetre,"replay")
				brevenge = gtk.Button("Revenge")
				brevenge.connect("clicked", self.passage,fenetre,"revenge")
				bbox.add(brevenge)
				bbox.add(breplay)
				bbox.add(bquit)
				text.show()
				bquit.show()
				breplay.show()
				brevenge.show()
				resultbox.add(text)
				resultbox.add(bbox)
				resultbox.show()
				bbox.show()
				self.grid.add(resultbox)
				return ""
			self.board.affiche()
			if self.joueurAct == self.player[0]:
				self.joueurAct = self.player[1]
			else:
				self.joueurAct = self.player[0]
			if isinstance(self.joueurAct , aiPlayerTTT):
				i,j = self.player[1].ai(self.board)
				print "ia a retourné " , i, j
				self.play(widget,evenement,i,j,fenetre)
				self.board.affiche()
				
	#methode qui permet soit de faire quitter la personne de rejouer ou de faire une revanche
	def passage(self , widget, fenetre, msg ):
		self.grid.hide()
		if msg == "quit":
			self.destroy(widget)
			return
		if msg == "replay":
			self.homePage(fenetre)
		else:
			self.constructionjeu(fenetre)
			
	def realPlayer(self ,widget,fenetre):
		self.player.append(Player("rond","O"))
		self.constructionjeu(fenetre)
		
	def aiPlayer(self ,widget,fenetre):
		self.player.append(aiPlayerTTT("rond","O"))
		self.constructionjeu(fenetre)

	def __init__(self,fenetre):
		self.color = gtk.gdk.Color('grey') 
		self.homePage(fenetre)
		
	def homePage(self,fenetre):
		
		self.player = [Player("croix","X")]
		#text pour le choix 
		self.choixl = gtk.Label("Voulez vous jouer contre un autre joueur ou contre une IA?")
		fenetre.add(self.choixl)
		#bouton pour un joueur
		self.bplayer = gtk.Button("Joueur")
		self.bplayer.connect("clicked", self.realPlayer , fenetre)
		fenetre.add(self.bplayer)
		#bouton pour l'ia
		self.bai = gtk.Button("AI")
		self.bai.connect("clicked", self.aiPlayer , fenetre)
		fenetre.add(self.bai)
		
		self.joueurAct = self.player[0]
		self.choixl.show()
		self.bplayer.show()
		self.bai.show()
		fenetre.show()
		
	def constructionjeu(self,fenetre):
		self.choixl.hide()
		self.bplayer.hide()
		self.bai.hide()
		self.grid = gtk.VBox(True,1)
		self.board = PlateauTTT(3)
		for i in range(self.board.nb):
			lineEvent = []
			self.line = gtk.HBox(True,1)    
		
			for j in range(self.board.nb):
				self.event = gtk.EventBox()
				self.event.modify_bg(gtk.STATE_NORMAL, self.color);
				self.event.connect("button_press_event", self.play , i, j ,fenetre)
				self.event.show()
				self.line.add(self.event)
				lineEvent.append(self.event)
			self.board.addLineEvent(lineEvent)
			self.grid.add(self.line)
			self.line.show()

		fenetre.add(self.grid)
		self.grid.show()
		fenetre.show()

	def run(self):
		gtk.main()

	
