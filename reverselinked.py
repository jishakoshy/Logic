# reverse a linked list ?!!!!

# input - 1->2->3->4->5->Null
# output - 5->4->3->2->1->Null

def reverselinked(self):
    prev = None
    cur = self.head
    nxt = cur.next

    while cur != None:
        # nxt = cur.next
        cur.next = prev
        prev = cur 
        cur = nxt
    cur = prev
    return cur



