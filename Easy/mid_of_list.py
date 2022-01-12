# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow
        '''
        ctr=0
        cur=head
        while(cur):
            cur=cur.next
            ctr+=1
        print(ctr)
        cur=head
        i=0
        while(i<(ctr//2)+1):
            head=cur
            cur=cur.next
            i+=1
        return head
        
        
        
    i        j
    [1,2,3,4,5]
    
    '''