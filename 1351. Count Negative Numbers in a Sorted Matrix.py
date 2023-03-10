class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row_idx, col_idx = 0, len(grid[0]) - 1

        ans = 0

        while row_idx < len(grid) and col_idx >= 0:
            if grid[row_idx][col_idx] < 0:
                ans += len(grid) - row_idx
                col_idx -= 1
            else:
                row_idx += 1

        return ans
