#!/usr/bin/env python

# CFG objects
from __init__ import *

# if var x is not alive on path btwn definition and exit node, then it is dead code
# eg. x = 1;  this is dead
#     y = 2;  
#     x = 3;  b/c x is redeclared b4 being used

def deadcode(graph):

  # vars that have been declared, but are unused 
  live_vars = set()

  # vars that have been used
  used_live_vars = set()

  # pairs of active vars and which line they refer to, permitting deletion of dead code
  #line_ref = []

  # set of nodes to work with
  work = set(graph.reachable_blocks())
 
  i=0

  while True and i < 10:
    
    live_vars = set()
    used_live_vars = set()

    for block in work:
      for statement in block.stmts:
        if statement.type == 'RETURN':
          used_live_vars.add(statement.var)
          live_vars.add(statement.var)
        else:
          if statement.var:
            live_vars.add(statement.var)
          if statement.rhs1:
            live_vars.add(statement.rhs1)
          if statement.rhs2:
            live_vars.add(statement.rhs2)


    
    new_vars = True
    while new_vars:
      new_vars = False
      for block in work:
        for statement in block.stmts:
          if statement.var in used_live_vars:
            if statement.rhs1 and statement.rhs1 not in used_live_vars:
              used_live_vars.add(statement.rhs1)
              new_vars = True
            if statement.rhs1 and statement.rhs2 not in used_live_vars:
              used_live_vars.add(statement.rhs2)
              new_vars = True

    dead_vars = live_vars - used_live_vars
    #print 'dead', dead_vars
    if not dead_vars:
      break

    # remove all dead statements
    for block in work:
      live_stmts = []
      #print 'live_stmts', live_stmts
      for statement in block.stmts:
        if statement.var not in dead_vars:
          live_stmts.append(statement)
        else:
          pass
          #print 'removing a statement', statement
      block.stmts = live_stmts

    i+=1
