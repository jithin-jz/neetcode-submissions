from typing import List

class ListNode:
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # Use a dummy head node to simplify operations
        self.head = ListNode()
        self.size = 0
    
    def get(self, index: int) -> int:
        """
        Return the value of the ith node (0-indexed).
        If the index is out of bounds, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        
        return curr.val
        
    def insertHead(self, val: int) -> None:
        """Insert a node with val at the head of the list."""
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1
        
    def insertTail(self, val: int) -> None:
        """Insert a node with val at the tail of the list."""
        new_node = ListNode(val)
        
        # Find the last node
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        
        curr.next = new_node
        self.size += 1
        
    def remove(self, index: int) -> bool:
        """
        Remove the ith node (0-indexed).
        If the index is out of bounds, return false, otherwise return true.
        """
        if index < 0 or index >= self.size:
            return False
        
        # Find the node before the one to remove
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        # Remove the node
        curr.next = curr.next.next
        self.size -= 1
        
        return True
        
    def getValues(self) -> List[int]:
        """Return an array of all the values in the linked list, ordered from head to tail."""
        result = []
        curr = self.head.next
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result