class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        st = set(jewels)
        counter = 0
        for stone in stones:
            if stone in st:
                counter += 1

        return counter