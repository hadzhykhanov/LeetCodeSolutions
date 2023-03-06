from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        memory = defaultdict(int)

        for char in s1:
            memory[char] += 1

        left, size = 0, len(memory)

        for right, cur_char in enumerate(s2):
            if cur_char not in memory:
                while left != right:
                    left_char = s2[left]

                    memory[left_char] += 1
                    if memory[left_char] == 1: size += 1
                    left += 1

                left += 1

            elif memory[cur_char] == 0:
                while memory[cur_char] != 1:
                    left_char = s2[left]

                    memory[left_char] += 1
                    if memory[left_char] == 1: size += 1
                    left += 1

                memory[cur_char] -= 1
                size -= 1

            else:
                memory[cur_char] -= 1
                if memory[cur_char] == 0: size -= 1
                if size == 0: return True

        return False