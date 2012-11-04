from basicblock import BasicBlock

class CFGraph():
  def __init__(self):
    self.root = None
    self.blocks = set()

  def reachable_blocks(self, start=None):
    """ Performs a search on the CFG and yields
    each basic block following the given block

    >>> from examples import *
    >>> set(simple_graph.reachable_blocks()) == set([b1, b2, b3, b4])
    True
    >>> dead_graph.blocks == set([b11, b12, b13, b14, b15])
    True
    >>> set(dead_graph.reachable_blocks()) == set([b11, b12, b13, b14])
    True
    """

    # Start at the root by default
    if not start:
      start = self.root
    
    # Keep track of visited nodes
    visited = set()

    # Next set of nodes to look at
    horizon = set([start])

    # Recursively yield the next set of blocks
    while horizon:
      block = horizon.pop()
      if block not in visited:
        yield block
        visited.add(block)

        # Add in the next set of blocks
        horizon.update(block.out_edges)

  def gen_graphviz(self):
    """ Returns a textual representation of
    the control flow graph that can be visualised
    using Graphviz
    
    >>> from examples import *
    >>> print simple_graph.gen_graphviz()
    digraph prog {
      node [shape=rectangle,fontname=Courier];
      L1 [label="L1:\\lb = i > 100;\\lif b goto L2;"];
      L1 -> L2;
      L1 -> LX1;
      L2 [label="L2:\\lreturn s;"];
      LX0 [label="LX0:\\li = 1;\\ls = 0;"];
      LX0 -> L1;
      LX1 [label="LX1:\\ls = s + 1;\\li = i + 1;"];
      LX1 -> L1;
    }
    """
    s = """digraph prog {
  node [shape=rectangle,fontname=Courier];"""
    for block in sorted(self.blocks,key=lambda x:x.label):
      s += '\n' # separate each block with newline
      s += block.gen_graphviz() # add the graphviz code for each block
    s += '\n}';
    return s

  def optimize(self):
    # Keep optimizing until we can't
    while True:
      if self.remove_jumps():
        continue # optimising
      if self.remove_unreachable():
        continue # optimising
      if self.remove_dead_code():
        continue # optimising

      break # stop optimising

  def remove_dead_code(self):
    pass

  def remove_unreachable(self):
    # Get the set of reachable blocks
    new_blocks = set(self.reachable_blocks())

    # Have we removed any blocks?
    if new_blocks == self.blocks:
      return False
    else:
      self.blocks = new_blocks
      return True

  def remove_jumps(self):
    """ Removes unnecessary jumps from the CFG

    >>> from examples import *
    >>> jump_graph.remove_jumps()
    True
    >>> len(jump_graph.blocks) == 1
    True
    """

    # Set of unoptimized blocks
    blocks = set(self.blocks)
    removed_jump = False

    # Remove jumps
    while blocks:
      block = blocks.pop()

      # Blocks with one in edge in the CFG can join with their in blocks
      #  if the in block has only this block as an out edge
      if len(block.in_edges) == 1:
        in_block = list(block.in_edges)[0]
        if in_block.out_edges == set([block]):
          joined_block = self.combine(in_block, block)
          removed_jump = True

          # Start over
          blocks = set(self.blocks)

    # Have we really removed any jumps?
    return removed_jump

  def combine(self, block1, block2):
    """ Combine two basic blocks into a single basic block.
    This block is assumed to be the first block.
    Raises an ValueError if the combination will not work"""

    # Will not work if the first block has a condition
    if block1.cond:
      raise ValueError("First block has a conditional jump, it cannot be combined.")
    # Or the second block has other in edges in the CFG
    if len(block2.in_edges) > 1:
      raise ValueError("The second block has muliple in edges in the CFG, it cannot be combined")
    # Or the blocks do not join in the CFG
    if not (block1.out_edges == set([block2]) and block2.in_edges == set([block1])):
      raise ValueError("First and second block are not connected in the CFG")

    # Combine code and use second block's condition
    #new_block = BasicBlock(block1.code+'\n'+block2.code, block1.label, block2.cond)
    new_block = BasicBlock(block1.stmts+block2.stmts, block1.label, block2.cond)

    # Use first block's in jumps
    new_block.in_edges = set(block1.in_edges)
    # Use second block's out jumps
    new_block.out_edges = set(block2.out_edges)

    # Update incoming edges
    for block in block1.in_edges:
      block.out_edges.remove(block1)
    for block in new_block.in_edges:
      block.out_edges.add(new_block)

    # Update outgoing edges
    for block in block2.out_edges:
      block.in_edges.remove(block2)
    for block in new_block.out_edges:
      block.in_edges.add(new_block)

    # Remove old blocks
    self.blocks.remove(block1)
    self.blocks.remove(block2)

    # Add new block
    self.blocks.add(new_block)
  
  def linearized_blocks(self):
    """ Returns blocks much like the reachable_blocks method.
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
    all_blocks = set(self.reachable_blocks())

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
    >>> print simple_graph.code_string()
    i = 1;
    s = 0;
    L1:
    b = i > 100;
    if b goto L2;
    s = s + 1;
    i = i + 1;
    goto L1;
    L2:
    return s;
    """

    # Linearized code string
    code = ""

    # The linearized set of reachable blocks
    if optimized:
      linearized_blocks = self.linearized_blocks()
    else:
      linearized_blocks = self.reachable_blocks()

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
      #code += '\n'.join([indent+c for c in block.code.splitlines()])+'\n'
      code += '\n'.join([indent+str(c) for c in block.stmts])+'\n'

      # Next block of code
      prev_block = block

    return code.rstrip()

  def __str__(self):
    return self.root.code
