# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        fast=dummy
        slow=dummy
        for i in range(1,n+2):
            fast=fast.next
            print(i)
        while(fast!=None):
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next
    
    '''
         s     f  
    [1,2,3,4,5]   n=2
    '''
        