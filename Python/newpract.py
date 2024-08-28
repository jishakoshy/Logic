# linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# insertion -> 3 types front,end,at middle
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def insertatend(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            currentnode = self.head
            while(currentnode.next):
                currentnode = currentnode.next
            currentnode.next = newnode

    def insertindex(self,data,index):
        newnode = Node(data)
        currentnode = self.head
        position = 0
        if position == index:
            self.insert(data)
        else:
            while(currentnode is not None and position + 1 != index):
                position += 1
                currentnode = currentnode.next
            
            if currentnode != None:
                newnode 

