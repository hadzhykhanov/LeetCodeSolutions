# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        curr_next = head.next
        while curr_next:
            item = curr_next.next
            curr_next.next = curr
            curr = curr_next
            curr_next = item

        head.next = None
        return curr
