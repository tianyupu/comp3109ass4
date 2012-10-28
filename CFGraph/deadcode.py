#!/usr/bin/env python

# CFG objects
from __init__ import *

# if var x is not alive on path btwn definition and exit node, then it is dead code
# eg. x = 1;  this is dead
#     y = 2;  
#     x = 3;  b/c x is redeclared b4 being used

def deadcode(graph):

  # set of vars with potential to have associated dead code
  unused_live_vars = set()

  # pairs of active vars and which line they refer to, permitting deletion of dead code
  line_ref = []

  # remove dead code from first block
  start = graph.root
  unused_live_vars = deadBlock(start,unused_live_vars)

  # continue through rest of graph
  x = downGraph(graph, graph.block.out_edges[0], deadBlock(block,unused_live_vars))
  return x

def downGraph(graph, block, unused_live_vars):
  if len(graph.block.out_edges) == 0:
    return unused_live_vars
  if len(graph.block.out_edges) == 1:
    x = downGraph(graph, graph.block.out_edges[0], deadBlock(block,unused_live_vars))
  else:
    x = downGraph(graph, graph.block.out_edges[0], deadBlock(block,unused_live_vars))
    i = 1
    while i >= len(graph.block.out_edges):
      x = x.union(downGraph(graph, graph.block.out_edges[i], deadBlock(block,unused_live_vars))
      i += 1
  return x

def deadBlock(block,unused_live_vars):
  for line in block:
    # if a var on lhs
      # if var is in unused_live_vars
        # the previous declaration is dead code line; remove it
      # else
        # add it to unused_live_vars
    # if a var is on the rhs
      # if var is in unused_live_vars
        # remove it from unused_live_vars
      # else
        # ignore it, it is just being used again
  return unused_live_vars

