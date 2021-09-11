class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linkedlist:
    def __init__(self):
        self.head=None

    def printlinkedlist (self):
        temp = self.head

        while (temp):
            print(temp.data)
            temp = temp.next

ll1 = linkedlist()
ll1.head = node(1)
second = node(2)
third =node(3)

ll1.head.next=second
second.next=third

ll1.printlinkedlist()
