#!/usr/bin/env python
# coding utf8
# exemple helloworld.py

from TicTacToe import *
from PlateauTTT import *
import pygtk
pygtk.require('2.0')
import gtk
import gtk.gdk
from PIL import ImageTk
import Tkinter as Tk
from PIL import Image

class ViewTTT:
  
  def play(self, widget, evenement, donnees, board,  i, j):
    result = board.joue(i, j, widget, self.joueurAct, self.player)
    if result != "Already played":
      if result == "win":
	self.buffer = gtk.TextBuffer(table=None)
	self.buffer.set_text("Congratulations player {0} you win".format(self.joueurAct))
	text = gtk.TextView(self.buffer)
	text.set_editable(False)
	hbox = gtk.HBox(True, 1)
	boutton = gtk.Button("Quitter")
	boutton.connect("clicked", self.destroy, None)
	hbox.add(text)
	hbox.add(boutton)
	text.show()
	boutton.show()
	self.vbox.add(hbox)
	hbox.show()
	return ""
      if result == "end":
	self.buffer = gtk.TextBuffer(table=None)
	self.buffer.set_text("It's a tie")
	text = gtk.TextView(self.buffer)
	text.set_editable(False)
	hbox = gtk.HBox(True, 1)
	boutton = gtk.Button("Quitter")
	boutton.connect("clicked", self.destroy, None)
	align = boutton.get_alignment()
	print align
	hbox.add(text)
	hbox.add(boutton)
	text.show()
	boutton.show()
	self.vbox.add(hbox)
	hbox.show()
	return ""
      if self.joueurAct == self.player[0]:
	self.joueurAct = self.player[1]
      else:
	self.joueurAct = self.player[0]
    
  def evnmt_delete(self, widget, evenement, donnees=None):
    print "Evenement delete survenu"
    return False
  '''def fin(self, widget, evenement, donnees=None):
    print "Evenement delete survenu"
    return False'''
  def destroy(self, widget, donnees=None):
    print "Evenement destroy survenu"
    gtk.main_quit()
  def __init__(self, board, player):
    self.player = player
    self.joueurAct = player[0]
    self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.fenetre.connect("delete_event", self.evnmt_delete)
    self.fenetre.connect("destroy", self.destroy)
    self.fenetre.set_border_width(10)
    self.fenetre.resize(622,622)
    self.vbox = gtk.VBox(True,1)
    #self.visual = gtk.gdk.Visual(1,gtk.gdk.VISUAL_STATIC_GRAY)
    #self.colormap = gtk.gdk.Colormap(self.visual, True)
    #self.vbox.set_colormap(self.colormap)
    self.color = gtk.gdk.Color('blue')
    for i in range(board.nb):
      self.hbox = gtk.HBox(True,1)    
      for j in range(board.nb):
	self.event = gtk.EventBox()
	self.event.modify_bg(gtk.STATE_NORMAL, self.color);
	self.event.connect("button_press_event", self.play , None, board, i, j)
	self.event.show()
	self.hbox.add(self.event)
      self.vbox.add(self.hbox)
      self.hbox.show()
    self.fenetre.add(self.vbox)
    self.vbox.show()
    self.fenetre.show()
  def boucle(self):
    gtk.main()
    

if __name__ == "__main__":
  game = TicTacToe()
  game.run()
	