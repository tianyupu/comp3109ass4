#!/usr/bin/env python

class BasicBlock():
  def __init__(self, code):
    self.code = code

    self.gen = set()
    self.kill = set()

    self.in_edges = set()
    self.out_edges = set()

  def gen_graphviz(self):
    pass

  def __str__(self):
    return self.code


class CFGraph():
  def __init__(self):
    self.root = None

  def gen_graphviz(self):
    pass

  def optimize(self):
    pass

  def remove_dead_code(self):
    pass

  def remove_unreachable(self):
    pass

  def remove_jumps(self):
    pass
  
  def __str__(self):
    return self.root.code
