from collections import defaultdict
from heapq import heappop, heapify


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        memory = defaultdict(int)
        out = [0] * k
        for word in words:
            memory[word] -= 1

        memory = [(value, key) for key, value in memory.items()]
        heapify(memory)

        return [heappop(memory)[1] for _ in range(k)]
    