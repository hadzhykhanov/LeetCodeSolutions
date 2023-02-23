from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cur_state = Counter(t)
        res_len, res_coords = None, None
        left = 0
        size = len(cur_state)

        for right, cur_char in enumerate(s):
            if cur_char in cur_state:
                cur_state[cur_char] -= 1

                if cur_state[cur_char] == 0:
                    size -= 1

                while size == 0:
                    cur_len = right - left + 1

                    if res_len is None or cur_len < res_len:
                        res_coords = (left, right + 1)
                        res_len = cur_len

                    left_char = s[left]

                    if left_char in cur_state:
                        cur_state[left_char] += 1
                        if cur_state[left_char] == 1:
                            size += 1

                    left += 1

        return s[res_coords[0]:res_coords[1]] if res_coords else ""
