from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, res = 0, 0
        memory = defaultdict(int)

        for right, right_item in enumerate(fruits):
            memory[right_item] += 1

            if len(memory) == 3:
                while len(memory) != 2:
                    left_item = fruits[left]

                    memory[left_item] -= 1
                    if memory[left_item] == 0:
                        memory.pop(left_item)

                    left += 1

            cur_fruits_count = right - left + 1
            if cur_fruits_count > res:
                res = cur_fruits_count

        return res
