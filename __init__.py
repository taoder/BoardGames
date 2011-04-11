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
	ttt = TicTacToe(box)
	ttt.run()
	destroy(None)

def delete_event( widget, event, data=None):
	print "Window closed!"
	return False

def destroy( widget, data=None):
	gtk.main_quit()

def run():
	window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	window.connect("delete_event", delete_event)
	window.connect("destroy", destroy)
	window.set_border_width(10)
	window.resize(642,632)
	print "ici"

	scrollwindow = gtk.ScrolledWindow()
	scrollwindow.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		
	
	subwindow = gtk.VBox()
	window.add(subwindow)
	subwindow.pack_start(scrollwindow,True,True,0)
	
	scrollwindow.show()
	windowjeu = gtk.VBox()
	label = gtk.Label("Appuyez sur le bouton pour lancer le truc")
	windowjeu.add(label)

	lanceur = gtk.Button("Lancer le truc")
	lanceur.connect("clicked", launch ,label , windowjeu)
	windowjeu.add(lanceur)		
	print "ici2"
	scrollwindow.add_with_viewport(windowjeu)
	#on n'affiche pas encore la truc box, seulement quand le truc est lancé
	label.show()
	lanceur.show()
	windowjeu.show()
	subwindow.show()
	window.show()
		
	main()	
	

def main():
	
	gtk.main() 
	print "ici3"   

