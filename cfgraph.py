class BasicBlock():
  def __init__(self, code):
    self.code = code

    self.gen = set()
    self.kill = set()

    self.in_edges = {}
    self.out_edges = {}

  def gen_graphviz(self):
    pass


class CFGraph():
  def __init__(self):
    self.root = None

  def gen_graphviz(self):
    pass

  def optimize(self):
    pass

  def remove_dead_code(self):
    pass

  def remove_unreachable(self):
    pass

  def remove_jumps(self):
    pass
