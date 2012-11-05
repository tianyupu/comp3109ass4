class Cond():
  def __init__(self, var, true_block, false_block):
    self.var = var
    self.true_block = true_block
    self.false_block = false_block

  def __str__(self):
    return 'if %s goto %s;' % (self.var, self.true_block.label)

class Statement():
  def __init__(self, stmt_node):
    """Creates a Statement object from a given stmt AST node.
    
    Note that IF statements are not covered, as they are 
    Cond objects. They will always occur at the end of a Basic
    Block, and their variable name can be accessed using 
    <instancename>.var."""

    self.var = None
    self.rhs1 = None
    self.rhs2 = None
    # stores the actual line of code for this statement
    self.code = ' '.join([n.text for n in stmt_node.children]) + ';'

    # if it's an assign statement of some sort,
    # then the destination variable (LHS) can be accessed via the
    # var attribute. depending on the type of assignment,
    # the RHS can have 1 or 2 operands. access them with rhs1
    # and rhs2. if rhs2 doesn't exist, then its value is None
    if stmt_node.token.text.startswith('ASSIGN'):
      self.type = 'ASSIGN'
      if stmt_node.token.text == 'ASSIGN1':
        var, eq, rhs1 = stmt_node.children
        rhs2 = None
      else:
        var, eq, rhs1, op, rhs2 = stmt_node.children
      self.var = var.text
      self.rhs1 = rhs1.text
      self.rhs2 = rhs2.text if rhs2 else None

    # if it's a return statement, then you can get
    # the name of the variable that is to be returned
    # by using the var attribute of this object also
    if stmt_node.token.text == 'RETURN':
      self.type = 'RETURN'
      retword, var = stmt_node.children
      self.var = var.text

  def __str__(self):
    return self.code

  def __repr__(self):
    return self.code

class BasicBlock():
  label_num = 0
  def __init__(self, stmts, label=None, cond=None):
    """Create a BasicBlock from a list of Statement objects."""
    # Remove unnecessary whitespace from code
    self.code = '\n'.join([str(stmt).strip() for stmt in stmts])
    #self.code = '\n'.join([line.strip() for line in code.strip().splitlines()])
    self.stmts = stmts # a list of statement objects

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
    given as a Statement object."""
    self.code += '\n' + str(stmt).strip()
    self.stmts.append(stmt)
  
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
