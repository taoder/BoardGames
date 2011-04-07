# -*- coding: utf-8 -*-
from player.thePlayer import Player
from base import *
from tictactoe import *

import pygtk
pygtk.require('2.0')
import gtk



def launch( widget, label, box):
	#lance le petit truc
	print "Appel de truc"
	widget.hide()
	label.hide()
	#plus besoin du bouton une fois le jeu lancé
	TicTacToe.run(box)
	print "Truc lancé!"

def delete_event( widget, event, data=None):
	print "Window closed!"
	return False

def destroy( widget, data=None):
	gtk.main_quit()

def runmainwindow():
	window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	window.connect("delete_event", delete_event)
	window.connect("destroy", destroy)
	window.set_border_width(10)
	window.resize(622,622)

	gdBox = gtk.VBox(False, 5)
	window.add(gdBox)	

	label = gtk.Label("Appuyez sur le bouton pour lancer le truc")
	gdBox.add(label)

	lanceur = gtk.Button("Lancer le truc")
	lanceur.connect("clicked", launch ,label , gdBox)
	gdBox.add(lanceur)		

	trucBox = gtk.VBox(False, 5)
	gdBox.add(trucBox)

	#on n'affiche pas encore la truc box, seulement quand le truc est lancé
	label.show()
	lanceur.show()
	gdBox.show()
	window.show()	
	main()	

def main():
	gtk.main()

def run():
	runmainwindow()

