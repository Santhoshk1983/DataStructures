class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = node(0)
a1 = node(1)
a2 = node(2)
a3 = node(3)

root.left = a1
root.right = a2
a1.left = a3