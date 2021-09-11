class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linkedlist:
    def __init__(self):
        self.head=None

ll1 = linkedlist()
ll1.head = node(1)
second = node(2)
third =node(3)

ll1.head.next=second
second.next=third

print(ll1.head.data)
print(ll1.head.next)
print(second.data)
print(third.data)