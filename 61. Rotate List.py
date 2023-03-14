class Solution:
    def get_size_of_linked_list(self, head):
        size = 1
        cur = head

        while cur.next:
            size += 1
            cur = cur.next

        return size, cur

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            linked_list_size, last = self.get_size_of_linked_list(head)
            k = k % linked_list_size

            if k == 0:
                return head

            first, second = head, head
            for _ in range(k + 1):
                second = second.next

            while second:
                second = second.next
                first = first.next

            kth_from_the_end = first.next
            first.next = None
            last.next = head
            return kth_from_the_end
