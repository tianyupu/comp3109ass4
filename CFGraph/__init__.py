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

  def add_edges(self, blocks):
    """ Adds given blocks to this blocks out edge set
    and adds this block to the given blocks' in edge set

    >>> b1 = BasicBlock('')
    >>> b2 = BasicBlock('')
    >>> b3 = BasicBlock('')
    >>> b1.add_edges([b2])
    >>> b2.add_edges([b1, b3])
    >>> 
    >>> b1.out_edges == set([b2])
    True
    >>> b1.in_edges == set([b2])
    True
    >>> b2.out_edges == set([b1, b3])
    True
    >>> b2.in_edges == set([b1])
    True
    >>> b3.out_edges == set()
    True
    >>> b3.in_edges == set([b2])
    True
    """
    # Add given blocks as out edges to this basic block
    self.out_edges.update(blocks)
    
    # Add this block as an in edge to given blocks
    for block in blocks:
      block.in_edges.add(self)

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
  
  def linearized_blocks(self):
    """ Returns blocks much like the basic_blocks method.
    However the blocks are returned in an optimal order.

    >>> from examples import *
    >>> blocks = simple_graph.linearized_blocks()
    >>> list(blocks) == [b1, b2, b3, b4]
    True
    >>> blocks = jump_graph.linearized_blocks()
    >>> list(blocks) == [b11, b13, b12, b14]
    True
    >>> blocks = dead_graph.linearized_blocks()
    >>> b15 not in blocks
    True
    """

    # Set of all blocks
    all_blocks = set(self.basic_blocks())

    # Set of blocks to explore
    cond = []
    non_cond = []
    if self.root.cond:
      cond.append(self.root)
    else:
      non_cond.append(self.root)
    # Set of visited blocks
    visited = set()

    while visited != all_blocks:
      # Yield all available conditionals first
      while cond:
        block = cond.pop()
        if block not in visited:
          yield block
          visited.add(block)

          # Add in the next set of blocks
          if block.cond:
            # Prefer false conditional jump next
            cond.append(block.cond.true_block)
            cond.append(block.cond.false_block)
          else:
            # Add next block to the non-conditional horizon
            non_cond.extend(block.out_edges)

      # Then a non-conditional jump
      while non_cond and not cond:
        block = non_cond.pop()
        if block not in visited:
          yield block
          visited.add(block)

        # Add in next blocks
        if not block.cond:
          # Add next block to the non-conditional horizon
          non_cond.extend(block.out_edges)
        else:
          # If we find a conditional exit
          # so we can optimise for conditional jumps first
          cond.append(block.cond.true_block)
          cond.append(block.cond.false_block)
    
  def code_string(self, indent='', optimized=True):
    """ Linearizes the CFG and
    returns a string of code

    >>> from examples import *
    >>> code = simple_graph.code_string()
    >>> code == '\\n'.join(map(str,
    ... [b1, b2.label+':', b2, b2.cond, b3,
    ... 'goto %s;'%b2.label, b4.label+':', b4]))
    True
    """

    # Linearized code string
    code = ""

    # The linearized set of basic blocks
    if optimized:
      linearized_blocks = self.linearized_blocks()
    else:
      linearized_blocks = self.basic_blocks()

    # Join together the blocks of code
    prev_block = None
    for block in linearized_blocks:
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
