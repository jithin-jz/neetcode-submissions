class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # Save the next node
            curr.next = prev        # Reverse the pointer
            prev = curr             # Move prev forward
            curr = next_node        # Move curr forward

        return prev