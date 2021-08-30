class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

n = Node('root')
p = Node('branch1')
q = Node('branch2')
r = Node('branch3')
n.add_child(p)
n.add_child(q)
p.add_child(r)
n.children
p.children

for c in n.children:
  print (c.data)

for x in p.children:
  print (x.data)