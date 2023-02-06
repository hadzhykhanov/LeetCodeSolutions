class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        memory = dict()

        for right in range(len(s)):
            if s[right] in memory:
                memory[s[right]] += 1

                while True:
                    memory[s[left]] -= 1
                    if memory[s[left]] == 0: memory.pop(s[left])
                    left += 1

                    if s[left - 1] == s[right]:
                        break

            else:
                memory[s[right]] = 1

            if len(memory) > res:
                res = len(memory)

        return res

