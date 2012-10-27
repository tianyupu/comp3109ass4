#!/usr/bin/env python

class BasicBlock():
  def __init__(self, code):
    # Remove unnecessary whitespace from code
    self.code = '\n'.join([line.strip() for line in code])

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

  def basic_blocks(self, block=None):
    """ Performs a search on the CFG and yields
    each basic block following the given block

    >>> from examples import *
    >>> set(simple_graph.basic_blocks()) == set([b1, b2, b3])
    True
    """

    # Start at the root by default
    if not block:
      block = self.root
    
    # Keep track of visited nodes
    visited = set()

    # Yield this block
    yield block
    visited.add(block)

    # Next set of nodes to look at
    horizon = set(block.out_edges)

    # Recursively yield the next set of blocks
    while horizon:
      next_block = horizon.pop()
      if next_block not in visited:
        yield next_block
        visited.add(next_block)
        horizon.update(next_block.out_edges)

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



if __name__ == '__main__':
  import doctest
  doctest.testmod()
