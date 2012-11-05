#!/usr/bin/env python

import sys
from collections import deque, defaultdict

import antlr3
from build.JumpLexer import JumpLexer
from build.JumpParser import JumpParser

import CFGraph

def main(filename):
  char_stream = antlr3.ANTLRFileStream(filename)
  tokens = antlr3.CommonTokenStream(JumpLexer(char_stream))
  parser = JumpParser(tokens)
  root = parser.prog()

  g = make_graph(root.tree)
  g.optimize()
  print g.code_string()

def gen_leaders(leaders):
  nexts = deque()
  for l in leaders:
    nexts.append(l)
  nexts.append(nexts.popleft())
  for i in xrange(len(leaders)):
    yield (leaders[i], nexts[i])

def make_graph(node):
  # a list of the index numbers of the leaders as 
  # discovered from the set of nodes from the root
  leaders = deque() 

  for lineno, child in enumerate(node.children):
    # first line in 'function'
    if lineno == 0 and child.token.text == 'STATEMENT':
      leaders.append(lineno)
    # statement begins with label
    elif len(child.children) == 2:
      lbl, stmt = child.children
      leaders.append(lineno)
    # if previous was goto, if or return, 
    # then this will be start of new block
    elif lineno > 0:
      prev_stmt = node.children[lineno-1]
      stmt_body = prev_stmt.children[-1]
      if stmt_body.token.text in ['GOTO', 'IF', 'RETURN']:
        leaders.append(lineno)

  stmt_no = deque(range(len(node.children))) # line numbers of all statements
  blocks = {} # blocks referenced by their index numbers
  lbl2index = {}
  links = defaultdict(set) # tracking the edges as we come across them
  while stmt_no: # while there are still unallocated statements
    lbl = None
    cond = None
    curr_lineno = stmt_no.popleft() # get the leftmost statement
    stmt_node = node.children[curr_lineno] # retrieve the statement node from the parser

    # if there's a label, retrieve that separately
    # stmt_body contains the subtree with the statement
    if len(stmt_node.children) == 2:
      lbl, stmt_body = stmt_node.children
      lbl = lbl.text
    else:
      stmt_body, = stmt_node.children
    # the actual line of code at this line number
    #code_line = ' '.join([n.text for n in stmt_body.children]) + ';'

    #s = CFGraph.Statement(stmt_body)

    # now we need to find the basic block that this statement belongs to
    # by examining each block number in turn and comparing it with the
    # statement number
    prev_leader, prev_nxt = 0, 0
    for leader, nxt_leader in gen_leaders(leaders):
      # if the current block no is larger, then the statement must belong
      # to the previous block that we saw
      if leader > curr_lineno:
        curr_blockno = prev_leader
        nxt_leader = prev_nxt
        break
      elif leader == curr_lineno:
        curr_blockno = leader
      prev_leader, prev_nxt = leader, nxt_leader

    # if this block hasn't been created yet, create it and we'll add
    # statements to it later
    if curr_blockno not in blocks:
      #new_block = CFGraph.BasicBlock(code_line, lbl, cond)
      new_block = CFGraph.BasicBlock([], lbl, cond)
      blocks[curr_blockno] = new_block
      lbl2index[new_block.label] = curr_blockno
      #continue # move onto the next statement; notice that we've consumed a statement from stmt_no

    # if the statement is an if, we want to get the expression and the target
    # of the conditional jump
    if stmt_body.token.text == 'IF':
      expr, target_lbl = stmt_body.children
      target_lbl = target_lbl.text
      # if the target has been created, and the block following this has 
      # also been created, then create the condition object and assign it to the block,
      # and update the links
      if target_lbl in lbl2index and nxt_leader in blocks:
        true_index = lbl2index[target_lbl]
        cond = CFGraph.Cond(expr.text, blocks[true_index], blocks[nxt_leader])
        blocks[curr_blockno].cond = cond
        links[curr_blockno].update([true_index, nxt_leader])
      else:
        # otherwise, we're not able to allocate this statement to a block
        # at this stage, so put it back on the unallocated statement queue
        stmt_no.append(curr_lineno)
      continue

    # if the statement is a goto, we want to get the target
    # of the jump
    if stmt_body.token.text == 'GOTO':
      target_lbl, = stmt_body.children
      # if the target block has been created, we can update the link to it
      if target_lbl.text in lbl2index:
        targ_index = lbl2index[target_lbl.text]
        links[curr_blockno].add(targ_index)
      else:
        # otherwise, put it back on the queue
        stmt_no.append(curr_lineno)
      continue
    
    # if we've gotten here, it means that the statement is not an if or goto
    # add it to the current block
    #blocks[curr_blockno].add_stmt(code_line)
    s = CFGraph.Statement(stmt_body)
    blocks[curr_blockno].add_stmt(s)

    # if we're at the last line before the start of the next block,
    # and this statement is not an if or goto, it means that we need
    # to add a link from this to the next block as it follows
    # directly after this one
    next_node = node.children[nxt_leader-1]
    if len(next_node.children) == 2:
      next_lbl, next_stmt_body = stmt_node.children
    else:
      next_stmt_body, = next_node.children
    if curr_lineno == nxt_leader-1 and next_stmt_body.token.text != 'RETURN':
      links[curr_blockno].add(nxt_leader)


  for index in blocks:
    l = links[index] # get all the indexes of outgoing link blocks
    blocks[index].add_edges([blocks[li] for li in l]) # add all the links

  # create the graph
  g = CFGraph.CFGraph()
  # blocks is hashed by lineno, so the first will always be the starting block
  g.root = blocks.values()[0]
  g.blocks.update(blocks.values()) # add all the blocks to the graph

  return g

# graph = parser.prog().graph

# while True:
#   graph.construct()
#   graph.print_CFG(sys.stdout)
#   if graph.perform_JE():
#     continue
#   if graph.perform_UC():
#     continue
#   if graph.perform_DCE():
#     continue
#   break

# graph.print_source(sys.stdout)

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print >> sys.stderr, 'Usage: %s <filename>' % sys.argv[0]
    sys.exit(1)
  main(sys.argv[1])
