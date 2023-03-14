class Solution(object):
    def read_list(self, head):
        digits = []

        cur = head
        while cur:
            digits.append(str(cur.val))
            cur = cur.next

        digits.reverse()
        return int("".join(digits))

    def create_list_from_str(self, number):
        head = ListNode(int(number[-1]))
        cur = head

        for idx in range(len(number) - 2, -1, -1):
            cur.next = ListNode(int(number[idx]))
            cur = cur.next

        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.create_list_from_str(str(self.read_list(l1) + self.read_list(l2)))


class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None)
        cur = dummy_head
        overflow = 0

        while l1 or l2 or overflow:
            first_val = l1.val if l1 else 0
            second_val = l2.val if l2 else 0

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

            cur_sum = first_val + second_val + overflow
            new_node = ListNode(cur_sum % 10)
            overflow = cur_sum // 10
            cur.next = new_node
            cur = cur.next

        return dummy_head.next