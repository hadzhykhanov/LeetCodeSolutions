# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode(next=head)
        first = new_head
        for _ in range(n + 1):
            first = first.next

        second = new_head
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return new_head.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode(next=head)

        cur_node = new_head
        while True:
            check_none = cur_node
            for _ in range(n + 1):
                check_none = check_none.next

            if check_none is None:
                cur_node.next = cur_node.next.next
                return new_head.next

            cur_node = cur_node.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_count = 0
        cur_node = head
        while cur_node:
            cur_node = cur_node.next
            node_count += 1

        if n == node_count:
            return head.next

        cur_node = head
        for _ in range(node_count - n - 1):
            cur_node = cur_node.next

        cur_node.next = cur_node.next.next
        return head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_count = 0
        cur_node = head
        while cur_node:
            cur_node = cur_node.next
            node_count += 1

        new_head = ListNode(next=head)
        new_head.next = head

        cur_node = new_head
        for _ in range(node_count - n):
            cur_node = cur_node.next

        cur_node.next = cur_node.next.next
        return new_head.next

