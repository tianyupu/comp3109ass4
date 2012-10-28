#!/usr/bin/env python

class BasicBlock():
  def __init__(self, code, label=None, cond=None):
    # Remove unnecessary whitespace from code
    self.code = '\n'.join([line.strip() for line in code.strip().splitlines()])

    # Label for the basic block
    if label == None:
      self.label = 'new_label' # TODO generate names
    else:
      self.label = label
    
    # Condition at the end of the basic block
    # None if no conditional jump
    self.cond = cond

    # Gen and kill sets
    self.gen = set()
    self.kill = set()

    # In and out edges in the CFG
    self.in_edges = set()
    self.out_edges = set()

  def gen_graphviz(self):
    pass

  def __str__(self):
    return self.code

  def __repr__(self):
    return "<BasicBlock: %s>" % str(self.label)

class Cond():
  def __init__(self, var, true_block, false_block):
    self.var = var
    self.true_block = true_block
    self.false_block = false_block

  def __str__(self):
    return 'if %s goto %s;' % (self.var, self.true_block.label)
    

class CFGraph():
  def __init__(self):
    self.root = None

  def basic_blocks(self, start=None):
    """ Performs a search on the CFG and yields
    each basic block following the given block

    >>> from examples import *
    >>> set(simple_graph.basic_blocks()) == set([b1, b2, b3, b4])
    True
    """

    # Start at the root by default
    if not start:
      start = self.root
    
    # Keep track of visited nodes
    visited = set()

    # Next set of nodes to look at
    horizon = [start]

    # Recursively yield the next set of blocks
    while horizon:
      block = horizon.pop()
      if block not in visited:
        yield block
        visited.add(block)

        # Add in the next set of blocks
        if block.cond:
          # Prefer false conditional jump next
          horizon.append(block.cond.true_block)
          horizon.append(block.cond.false_block)
        else:
          horizon.extend(block.out_edges)

  def gen_graphviz(self):
    pass

  def optimize(self):
    pass

  def remove_dead_code(self):
    pass

  def remove_unreachable(self):
    pass

  def remove_jumps(self):
    """ Removes unnecessary jumps from the CFG
    """

    pass
  
  def linearize(self, indent=''):
    """ Linearizes the CFG and
    returns a string of code

    >>> from examples import *
    >>> code = simple_graph.linearize()
    >>> code == '\\n'.join(map(str,
    ... [b1, b2.label+':', b2, b2.cond, b3,
    ... 'goto %s;'%b2.label, b4.label+':', b4]))
    True
    """

    # Linearized code string
    code = ""

    # Join together the blocks of code
    prev_block = None
    for block in self.basic_blocks():
      # Add jump from the previous block if necessary
      if prev_block:
        jumps = prev_block.out_edges - set([block])
        
        # Conditional jump cases
        if prev_block.cond:
          cond = prev_block.cond
          if len(jumps) == 1 and prev_block.cond:
            code += indent+str(cond)+'\n'
          elif len(jumps) == 2:
            code += indent+str(cond)+'\n'
            code += indent+'goto %s\n' % cond.false.label
        
        # Non-conditional jump cases
        else:
          if len(jumps) == 1:
            code += indent+'goto %s;\n' % jumps.pop().label

      # Add labels if necessary
      if block.in_edges - set([prev_block]) != set():
        code += '%s:\n' % block.label
      
      # Add block code with indentation
      code += '\n'.join([indent+c for c in block.code.splitlines()])+'\n'

      # Next block of code
      prev_block = block

    return code.rstrip()


  def __str__(self):
    return self.root.code



if __name__ == '__main__':
  import doctest
  doctest.testmod()
