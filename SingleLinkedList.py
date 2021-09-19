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

    def DelNode(self,data):
        del_data = data
        flag=0
        list_length=0
        data_list_num=0
       
       # Check the data availability in linked list

        while(self.head):
            list_length = list_length+1
            if (self.head.data == del_data):
                flag=1
                data_list = list_length -1
            self.head = self.head.next
        if flag==1:
            print("\nData is available for deletion. List length is ",list_length)
            print("Data available in list position -> ",data_list,"\n")
        else:
            print("\nData is not available in linked list. List length is ",list_length)


     # Check if its a first & only node then delete
        print("data_list ",data_list)
        print("List length", list_length)
        if (data_list==0 and list_length==0):
            self.head=None

    # Check if data is a last node and delete

        while(self.head):
            if self.head.data == del_data:
                break
            prev = self.head
            next = self.head.next

            prev.next = next
            next = next.next







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

ll1.DelNode(2)
ll1.printlinkedlist()