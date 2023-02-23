import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            first_max_stone = -heapq.heappop(stones)
            second_max_stone = -heapq.heappop(stones)

            if first_max_stone - second_max_stone != 0:
                heapq.heappush(stones, -(first_max_stone - second_max_stone))

        return -stones[0] if stones else 0