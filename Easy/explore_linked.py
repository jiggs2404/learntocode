class Node:
    def _init_(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:
    def _init_(self):
        self.head = None
        self.tail = None
    """
    head, tail
    curr = [7 | ]
    head= None
    """
        
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while (cur):
            if(i == index):
                return cur.val
            i+=1
            cur = cur.next
        return -1

    def addAtHead(self, val: int) -> None:
        cur = Node(val)
        '''
        if list is not empty
        if list is empty
        '''
        if self.head is None:
            self.head = cur
            self.tail = cur
        else:
            cur.next = self.head
            self.head = cur

    def addAtTail(self, val: int) -> None:
        cur = Node(val)
        if self.tail:
            self.tail.next = cur
            self.tail = cur
        else:
            self.head = cur
            self.tail = cur

    def addAtIndex(self, index: int, val: int) -> None:
        """
        index=0, last
        toInsert = [7 | ]-> null
        
        [1 | ]->[2 | ]->[3 | ]->[4 | ]->[5 | ] ->null
        """
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        i = 0
        node = Node(val)
        while cur:
            if i == index-1:
                nextnode = cur.next
                cur.next = node
                node.next = nextnode
                if not nextnode:
                    self.tail = node
                return
            cur = cur.next
            i += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        """
        1. Head: head is not existing, 
        2. tail
        3. any other
        """
        if (index==0):
            if self.head:
                if self.head == self.tail:
                    self.tail = self.tail.next
                self.head = self.head.next
            return
        cur = self.head
        i = 0
        while cur:
            if i == index-1:
                if cur.next:
                    cur.next = cur.next.next
                    if not cur.next:
                        self.tail = cur
                return
            cur = cur.next
            i += 1
        return
    


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)