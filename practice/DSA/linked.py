class Linkedlist:
    def insertatfirst(self,newnode):
        if self.head == None:
            self.head = newnode
        else:
            while self.head != None:
                newnode = self.head

