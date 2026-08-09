from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        # Dummy node. The actual first node is self.head.next
        self.head = ListNode()
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

        # Stop at the node BEFORE the target
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