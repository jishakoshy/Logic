# Instantiation of a Node Object:

# The expression Node(data) creates a new instance of the Node class.
# This instance represents a node in a linked list.
# __init__ Method Invocation:

# As soon as the instance is created, Python automatically calls the __init__ method of the Node class with the provided data parameter.
# Inside the __init__ method, the attributes of the node (self.data and self.next) are initialized with the provided data and None respectively.
# Data Assignment:

# The data parameter passed during the instantiation (Node(data)) is assigned to the data attribute of the newly created node (self.data = data).
# Next Pointer Initialization:

# Since the next attribute is initialized to None in the __init__ method, the newly created node's next attribute is automatically set to None.
# In summary, executing new_node = Node(data) instantiates a new node object with the provided data, where the data attribute of the node is initialized with the value passed in, and the next attribute is set to None by default.


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def insertionAtBegin(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        else:
            newnode = self.head
            self.head =newnode

    def insertionAtend(self,data):
        newnode = Node(data)
        if self.head is None:
            self.data = newnode
            return
        else:
            current_node = self.head
            while(current_node.next):
                current_node = current_node.next

            current_node = newnode

    def insertionAtindex(self,data,index):
        newnode = Node(data)
        

        
        