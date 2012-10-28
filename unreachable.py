#!/usr/bin/env python

# CFG objects
from __init__ import *

# takes in arguement of CFG
def reachable_nodes(graph):

  # set of reachable nodes
  reachable = set()
  
  # our work set
  work = set()
  work.add(graph.root)

  # iterate while work set is not empty
  while len(work) > 0:

    # the work set is reachable
    reachable = reachable.union(work)

    # add all reachable blocks from current work block to reachable
    # remove all 'reachable' parts from work to avoid endless loop
    for block in work:
      work = work.union(block.out_edges)-reachable
  
  return reachable

