# from collections import defaultdict, Counter
#
#
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         cur_state = Counter(t)
#         res_len, res_coords = None, (0, 0)
#         left = 0
#         size = len(cur_state)
#
#         for right, cur_char in enumerate(s):
#             if cur_char in cur_state:
#                 cur_state[cur_char] -= 1
#                 if cur_state[cur_char] == 0:
#                     size -= 1
#
#                 if size == 0:
#                     print(left, right)
#                     while size == 0:
#                         left_char = s[left]
#
#                         if left_char in cur_char:
#                             cur_state[left_char] += 1
#                             if cur_state[left_char] == 1:
#                                 size += 1
#
#                         left += 1
#
#                     if res_len is None or right - left < res_len:
#                         res_coords = (left - 1, right + 1)
#                         res_len = right - left
#
#         return s[res_coords[0]:res_coords[1]]
#