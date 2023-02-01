class Solution:
    @staticmethod
    def check_coords(i, j, grid):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])

    @staticmethod
    def get_coords(i, j):
        return [(i, j - 1), (i - 1, j)]

    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for __ in range(m)]
        grid[0][0] = 1

        for i in range(m):
            for j in range(n):
                for first_coord, second_coord in self.get_coords(i, j):
                    if self.check_coords(first_coord, second_coord, grid):
                        grid[i][j] += grid[first_coord][second_coord]

        return grid[m - 1][n - 1]
