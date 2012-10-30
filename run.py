#!/usr/bin/env python

import sys
from collections import deque, defaultdict
from subprocess import call

import antlr3
from build.JumpLexer import JumpLexer
from build.JumpParser import JumpParser

import CFGraph

def main(filename):
  char_stream = antlr3.ANTLRFileStream(filename)
  tokens = antlr3.CommonTokenStream(JumpLexer(char_stream))
  parser = JumpParser(tokens)
  root = parser.prog()

  #x = [n.text for n in root.tree.children[2].children[-2].children]
  #print "".join(x)
  g = make_graph(root.tree)
  print g.root
  print g.blocks
  f = open("run.dot", "w")
  f.write(g.gen_graphviz())
  f.close()
  call("dot -T png run.dot -o run.png", shell=True)

def make_graph(node):
  # a list of the index numbers of the leaders as 
  # discovered from the set of nodes from the root
  leaders = deque() 
  nxt_leads = deque()

  for lineno, child in enumerate(node.children):
    # first line in 'function'
    if lineno == 0 and child.token.text == 'STATEMENT':
      leaders.append(lineno)
      nxt_leads.append(lineno)
    # statement begins with label
    elif len(child.children) == 2:
      lbl, stmt = child.children
      leaders.append(lineno)
      nxt_leads.append(lineno)
    # if previous was goto, if or return, 
    # then this will be start of new block
    elif lineno > 1:
      prev_stmt = node.children[lineno-1]
      stmt_body = prev_stmt.children[-1]
      if stmt_body.token.text in ['GOTO', 'IF', 'RETURN']:
        leaders.append(lineno)
        nxt_leads.append(lineno)

  nxt_leads.rotate(-1)
  blocks = {} # blocks referenced by their index numbers
  lbl2index = {}
  links = defaultdict(set) # tracking the edges as we come across them
  while leaders:
    print "LEADERS:", leaders
    print "BLOCKS SO FAR:", blocks
    print "LBLS SO FAR:", lbl2index
    curr_lineno = leaders.popleft()
    next_lineno = nxt_leads.popleft()
    finished = False
    code = []
    lbl = None
    cond = None
    links[curr_lineno].add(next_lineno) # update the outgoing link
    if next_lineno < curr_lineno:
      next_lineno = len(node.children)-1
    if next_lineno == curr_lineno:
      nodes = [node.children[curr_lineno]]
    else:
      nodes = node.children[curr_lineno:next_lineno]
    for stmt_node in nodes:
      if len(stmt_node.children) == 2:
        # if this statement has a label, note that down
        lbl, stmt_body = stmt_node.children
        lbl2index[lbl.text] = curr_lineno
      else:
        stmt_body, = stmt_node.children
      # otherwise, examine the actual body of this statement
      if stmt_body.token.text == 'IF':
        expr, target_lbl = stmt_body.children
        # the block that we want to link to has not been created yet
        if target_lbl.text in lbl2index:
          true_index = lbl2index[target_lbl.text]
        else:
          break
        if true_index not in blocks or next_lineno not in blocks:
          break
        cond = CFGraph.Cond(expr.text, blocks[true_index], blocks[next_lineno])
        finished = True
      if stmt_body.token.text == 'GOTO':
        target_lbl, = stmt_body.children
        targ_index = lbl2index[target_lbl.text]
        links[curr_lineno].add(targ_index)
        finished = True
      code.append(' '.join([n.text for n in stmt_body.children]))
    # we've gone through all statements without hitting if or goto
    if len(code) == next_lineno-curr_lineno:
      finished = True
    elif len(code) == 1 and next_lineno == curr_lineno:
      finished = True
    if finished:
      code_str = ';\n'.join(code) + ';\n'
      blocks[curr_lineno] = CFGraph.BasicBlock(code_str, lbl, cond)
      continue
    leaders.append(curr_lineno)
    nxt_leads.append(next_lineno)

  for index in blocks:
    l = links[index] # get all the indexes of outgoing link blocks
    blocks[index].add_edges([blocks[li] for li in l]) # add all the links

  g = CFGraph.CFGraph()
  g.root = blocks.values()[0]
  g.blocks.update(blocks.values())

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
