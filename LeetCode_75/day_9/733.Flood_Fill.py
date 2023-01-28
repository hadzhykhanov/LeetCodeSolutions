from queue import Queue


class Solution:
    """bfs iterative"""
    @staticmethod
    def get_neighbors(x, y):
        return [(x + 1, y), (x - 1, y),
                (x, y + 1), (x, y - 1)]

    @staticmethod
    def check_coords(coord_x, coord_y, image, prev_color, ):
        return (0 <= coord_x < len(image)) and (0 <= coord_y < len(image[0])) and (
                    image[coord_x][coord_y] == prev_color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        prev_color = image[sr][sc]
        que = Queue()
        if prev_color != new_color:
            que.put((sr, sc))

        while que.qsize() != 0:
            coord_x, coord_y = que.get()
            image[coord_x][coord_y] = new_color

            for x, y in self.get_neighbors(coord_x, coord_y):
                if self.check_coords(x, y, image, prev_color):
                    que.put((x, y))

        return image


class Solution:
    """dfs iterative"""
    @staticmethod
    def get_neighbors(x, y):
        return [(x + 1, y), (x - 1, y),
                (x, y + 1), (x, y - 1)]

    @staticmethod
    def check_coords(coord_x, coord_y, image, prev_color):
        return (0 <= coord_x < len(image)) and (0 <= coord_y < len(image[0])) and (
                    image[coord_x][coord_y] == prev_color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        prev_color = image[sr][sc]
        stack = [(sr, sc)]

        if prev_color != new_color:
            while stack:
                coord_x, coord_y = stack.pop()
                image[coord_x][coord_y] = new_color

                for x, y in self.get_neighbors(coord_x, coord_y):
                    if self.check_coords(x, y, image, prev_color):
                        stack.append((x, y))

        return image


from queue import Queue


class Solution:
    """dfs recursion"""
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        def get_neighbors(x, y):
            return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        def check_coords(coord_x, coord_y):
            return (0 <= coord_x < len(image)) and (0 <= coord_y < len(image[0])) and (
                    image[coord_x][coord_y] == prev_color)

        def dfs(x, y):
            image[x][y] = new_color
            for coord_x, coord_y in get_neighbors(x, y):
                if check_coords(coord_x, coord_y):
                    dfs(coord_x, coord_y)

        prev_color = image[sr][sc]
        if prev_color != new_color:
            dfs(sr, sc)

        return image







