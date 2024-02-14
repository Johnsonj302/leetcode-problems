class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nextnode = head.next
            head.next = prev
            prev = head
            head = nextnode
        return prev