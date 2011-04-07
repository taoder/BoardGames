#-*- coding: utf-8 -*-

class CaseTTT:
  def __init__(self, value):
    self.value = value
  def getValue(self):
    return self.value
  def setValue(self, value):
    self.value = value
  def __repr__(self):
    return self.value