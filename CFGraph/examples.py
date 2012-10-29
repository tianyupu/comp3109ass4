#!/usr/bin/env python

# CFG objects
from __init__ import *

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

