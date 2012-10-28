# takes in arguement of CFG
def reachable_nodes(graph):
  reachable = set()
  work = set()
  work.add(graph.root)
  while len(work) > 0:
    reachable = reachable.union(work)
    for block in work:
      work = work.union(block.out_edges)-reachable
  return reachable

