# Basic Traversal for a Linked list, doubly linked list 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for doubly-linked list.
class Node:   
    def __init__(self, val, prev, next):
            self.val = val
            self.prev = prev
            self.next = next

#------------------------------------------------------------------------------------------------------

head = ListNode(1)                                  # ->1->2->3->None
head.next = ListNode(2)
head.next.next = ListNode(3)

temp = head

k = 0
while temp:
    if temp.next is None: k = temp.val
    temp = temp.next

print(k) #To verify, this traverses till the end and the fact that None has no value to return

#----------------------------------------------------------------------------------------------------------

head2 = Node(1, None, None)                   # None<-1<->2<->3->None
head2.next = Node(2, head2, None)
head2.next.next = Node(3, head2.next, None)

temp = head2

while temp.next:    # To stop before None
    temp = temp.next

while temp.prev:
     temp = temp.prev
    
print(temp.val)     # Went from 1 to 3 and back to 1