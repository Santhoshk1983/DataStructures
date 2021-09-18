class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linkedlist:
    def __init__(self):
        self.head=None


    # Traversing linked list
    def printlinkedlist (self): 
        temp = self.head
        
        while (temp):

            print(temp.data,end="")
            if temp.next != None:
                print("->",end="")
            temp = temp.next
        print ("\n")

    # Inserting as Header Node
    def HeaderNodeAdd (self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Inserting after a given node
    def AddNodeInbetween (self,prev_node,new_data):
        if prev_node is None:
            print("Can't insert as there are no previous node. Use HeaderNodeAdd")
            return
        new_node = node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def AddTail (self,new_data):

        new_node = node(new_data)
        if self.head==None:
            self.head=new_node
            return
        else :
            temp =self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node


ll1 = linkedlist()
ll1.head = node(1)
second = node(2)
third =node(3)

ll1.head.next=second
second.next=third
ll1.printlinkedlist()

ll1.HeaderNodeAdd(0)
ll1.printlinkedlist()

ll1.AddNodeInbetween(ll1.head.next,5)
ll1.printlinkedlist()

ll1.AddTail("X")
ll1.printlinkedlist()