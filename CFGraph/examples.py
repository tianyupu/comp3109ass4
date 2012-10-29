#!/usr/bin/env python
from copy import deepcopy

# CFG objects
from __init__ import *

graphs = {}

# The example Control Flow Graph
# from the assignment spec.

b4 = BasicBlock("""
    return s;""", 'L2')

b3 = BasicBlock("""
    s = s + 1;
    i = i + 1;""", 'LX1')

b2 = BasicBlock("""
    b = i > 100;""", 'L1',
    Cond('b', b4, b3))

b1 = BasicBlock("""
    i = 1;
    s = 0;""", 'LX0')

simple_graph = CFGraph()
simple_graph.root = b1

b1.add_edges([b2])
b2.add_edges([b3, b4])
b3.add_edges([b2])

simple_graph.blocks.update([b1, b2, b3, b4])
graphs['simple'] = simple_graph

# A Control Flow Graph
# for testing linearization

b14 = BasicBlock("""
    return x;""", 'L4')

b13 = BasicBlock("""
    x = x + 3""", 'L3')

b12 = BasicBlock("""
    x = x + 2""", 'L2')

b11 = BasicBlock("""
    x = 0""", 'L1')

jump_graph = CFGraph()
jump_graph.root = b11

b11.add_edges([b13])
b13.add_edges([b12])
b12.add_edges([b14])

jump_graph.blocks.update([b11, b12, b13, b14])
graphs['jump'] = jump_graph

# A Control Flow Graph
# for testing dead code

b15 = BasicBlock("""
    x = 100""", 'L5')

dead_graph = deepcopy(jump_graph)

dead_graph.blocks.add(b15)
graphs['dead'] = dead_graph
