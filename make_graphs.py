#!/usr/bin/env python
from subprocess import call
import sys

from CFGraph import examples

DOT_CMD = "dot -T png {name}.dot -o {name}.png"

for name, graph in examples.graphs.items():
  f = open("%s.dot" % name, "w")
  f.write(graph.gen_graphviz())
  f.close()
  call(DOT_CMD.format(name=name), shell=True)
