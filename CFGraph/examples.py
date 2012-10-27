#!/usr/bin/env python

# CFG objects
from __init__ import *

# The example Control Flow Graph
# from the assignment spec.

b1 = BasicBlock("""
    i = 1;
    s = 0;
    b = 1 > 100;
    if b goto L2;""")

b2 = BasicBlock("""
    L2: return s;""")

b3 = BasicBlock("""
    s = s + 1;
    i = i + 1;""")

simple_graph = CFGraph()

simple_graph.root = b1
simple_graph.root.out_edges.update([b2, b3])
simple_graph.root.in_edges.add(b2)

