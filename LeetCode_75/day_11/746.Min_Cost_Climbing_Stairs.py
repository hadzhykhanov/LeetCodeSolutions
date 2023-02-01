class Solution:
    """iterative"""
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])

        return cost[-1]

class Solution:
    """recursive"""
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def recursion(i):
            cost[i] += min(cost[i - 1], cost[i - 2])
            if i < len(cost) - 1:
                recursion(i + 1)

        cost.append(0)
        recursion(2)
        return cost[-1]
