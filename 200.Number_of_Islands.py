class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_neighbors(x, y):
            return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        def check_coords(coord_x, coord_y):
            return (0 <= coord_x < len(grid)) and (0 <= coord_y < len(grid[0])) and (grid[coord_x][coord_y] == "1")

        def dfs(coord_x, coord_y):
            grid[coord_x][coord_y] = "0"

            for x, y in get_neighbors(coord_x, coord_y):
                if check_coords(x, y):
                    dfs(x, y)

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    counter += 1

        return counter
