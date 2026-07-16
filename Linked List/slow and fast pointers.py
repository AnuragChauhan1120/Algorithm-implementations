# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The slow and fast pointer is highly modifiable and helps in various kinds of problem related to linked list structures

#-----------------------------------------------------------------------------------------------------------------

head = ListNode(1)                                  # ->1->2->3->None
head.next = ListNode(2)
head.next.next = ListNode(3)

slow = head
fast = head


while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if fast == slow : break

if fast == slow: print('Loop Found')
else: print('No loop found')

#-----------------------------------------------------------------------------------------------------------

head2 = ListNode(1)                                 # ->1->2->3-> Points to 2
head2.next = ListNode(2)                            
head2.next.next = ListNode(3)
head2.next.next = head2.next

slow = head2
fast = head2

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if fast == slow : break

if fast == slow: print('Loop Detected')
else: print('No loop found')