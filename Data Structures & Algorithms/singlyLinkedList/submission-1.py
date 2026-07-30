from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode()  # dummy head
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        
        return curr.val
    
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1
    
    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        
        curr.next = new_node
        self.size += 1
    
    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        curr.next = curr.next.next
        self.size -= 1
        return True
    
    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result
    
    # Optional: Additional helper methods
    def __len__(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        values = self.getValues()
        return " -> ".join(map(str, values))
    
    def search(self, val: int) -> int:
        """Return the index of the first occurrence of val, or -1 if not found."""
        curr = self.head.next
        index = 0
        while curr is not None:
            if curr.val == val:
                return index
            curr = curr.next
            index += 1
        return -1