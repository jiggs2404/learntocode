# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1=list1
        t2=list2
        t3=None
        if(t1==None):
            return list2
        if(t2==None):
            return list1
        while(t1!=None and t2!=None):
            print(t1.val)
            if(t1.val>t2.val):
                t3=self.append(t3,t2.val)
                t2=t2.next
            else:
                t3=self.append(t3,t1.val)
                t1=t1.next
        while(t1!=None):
            t3=self.append(t3,t1.val)
            t1=t1.next
        while(t2!=None):
            t3=self.append(t3,t2.val)
            t2=t2.next
        return t3
                
    def append(self, head, data):
        curr = head
        newNode = ListNode(data)

        if head is None:
            head = newNode
            return head

        while curr.next != None:
            curr = curr.next

        curr.next = newNode

        return head
                    
            