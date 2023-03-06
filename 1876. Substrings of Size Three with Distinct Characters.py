class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        memory = dict()
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in memory:
                memory[s[right]] += 1
            else:
                memory[s[right]] = 1

            if right - left == 3:
                memory[s[left]] -= 1
                if memory[s[left]] == 0: memory.pop(s[left])

                left += 1

            if len(memory) == 3:
                res += 1

        return res
