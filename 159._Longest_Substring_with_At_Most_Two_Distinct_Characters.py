from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """Given a string s, return the length of the longest substring
        that contains at most two distinct characters."""
        memory = defaultdict(int)
        left, res = 0, 0

        for right, cur_char in enumerate(s):
            memory[cur_char] += 1

            while len(memory) > 2:
                left_char = s[left]

                memory[left_char] -= 1
                if memory[left_char] == 0:
                    memory.pop(left_char)

                left += 1

            res = max(right - left + 1, res)

        return res
