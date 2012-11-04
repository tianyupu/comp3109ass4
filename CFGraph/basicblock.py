class Cond():
  def __init__(self, var, true_block, false_block):
    self.var = var
    self.true_block = true_block
    self.false_block = false_block

  def __str__(self):
    return 'if %s goto %s;' % (self.var, self.true_block.label)

class BasicBlock():
  label_num = 0
  def __init__(self, code, label=None, cond=None):
    """Create a BasicBlock from a string of statements."""
    # Remove unnecessary whitespace from code
    self.code = '\n'.join([line.strip() for line in code.strip().splitlines()])

    # Label for the basic block
    if label == None:
      self.label = BasicBlock.gen_label() # TODO generate names
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

  def add_stmt(self, stmt):
    """Add a single statement to the end of this BasicBlock,
    given as a string."""
    self.code += '\n' + stmt.strip()
  
  @staticmethod
  def gen_label():
    label = "LX%s" % BasicBlock.label_num
    BasicBlock.label_num += 1
    return label

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
    c = self.code

    # add the condition's code to the graphviz output
    if self.cond:
      c += '\n' + str(self.cond)
    c = c.replace('\n', '\\l')

    links = [] # stores each line in a list
    node_def = '  {label} [label="{label}:\\l{code}"];' # template for node labelling
    links.append(
        node_def.format(label=self.label, code=c))

    # append each outlink to the list of links
    for block in sorted(self.out_edges,key=lambda x:x.label):
      links.append('  %s -> %s;' % (self.label, block.label))

    # join them together and return the graphviz code for this block
    return '\n'.join(links)

  def __str__(self):
    return self.code

  def __repr__(self):
    return "<BasicBlock: %s>" % str(self.label)


