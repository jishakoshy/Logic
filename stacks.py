# stack implementation using linked list

# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        
# class Stack:
#     def __init__(self,data):
#         self.head = data

#     def push(self,data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             newnode = Node(data)
#             newnode.next = self.head
#             newnode = self.head

#     def pop(self):
#         if self.head is None:
#             return None
#         else:
#             popped_node = self.head
#             self.head = self.head.next
#             popped_node.next = None
#             return popped_node.data
        
#     def peek(self):
#         if self.head is None:
#             return None
#         else:
#             return self.head.data
        
#     def display(self):
#         iternode = self.head
#         if self.head is None:
#             return None
#         else:
#             while iternode != None:
#                 print(iternode.data,end="")
#                 if iternode.next != None:
#                     print("iternode.data")    
#             return



# implementing stack using array

def stack():
    stack = []
    return stack

def is_empty():
    return len(stack) == 0

def push(item):
    stack.append(item)
    return stack
def pop():
    stack.pop()
    return stack

def peek():
    return stack[len(stack)-1]









