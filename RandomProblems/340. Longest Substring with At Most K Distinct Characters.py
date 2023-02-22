from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """Given a string s and an integer k, return the length of the longest
        substring of s that contains at most k distinct characters."""
        memory = defaultdict(int)
        left, res = 0, 0

        for right, cur_char in enumerate(s):
            memory[cur_char] += 1

            while len(memory) > k:
                left_char = s[left]

                memory[left_char] -= 1
                if memory[left_char] == 0:
                    memory.pop(left_char)

                left += 1

            res = max(right - left + 1, res)

        return res
