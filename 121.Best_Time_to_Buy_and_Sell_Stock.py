class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        out = 0
        for i in range(1, len(prices)):
            item = prices[i]
            prices[i] -= curr_min
            if out < prices[i]:
                out = prices[i]
            if item < curr_min:
                curr_min = item

        return out
