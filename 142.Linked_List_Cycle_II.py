# https://blog.devgenius.io/leetcode-142-linked-list-cycle-ii-7cc3e587b6a0
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                break
        else:
            return None

        while head is not slow:
            head = head.next
            slow = slow.next
        else:
            return head