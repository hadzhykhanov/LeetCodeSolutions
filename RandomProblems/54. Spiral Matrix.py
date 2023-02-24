class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """using padding"""
        out = []
        row_count, columns_count = len(matrix), len(matrix[0])
        required_size = row_count * columns_count

        for i in range(row_count):
            matrix[i].insert(0, None)
            matrix[i].append(None)

        matrix.insert(0, [None] * (columns_count + 1))
        matrix.append([None] * (columns_count + 1))

        i, j = 1, 1
        while len(out) != required_size - 1:

            while matrix[i][j + 1] is not None:
                out.append(matrix[i][j])
                matrix[i][j] = None
                j += 1

            while matrix[i + 1][j] is not None:
                out.append(matrix[i][j])
                matrix[i][j] = None
                i += 1

            while matrix[i][j - 1] is not None:
                out.append(matrix[i][j])
                matrix[i][j] = None
                j -= 1

            while matrix[i - 1][j] is not None:
                out.append(matrix[i][j])
                matrix[i][j] = None
                i -= 1

        out.append(matrix[i][j])
        return out


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """no padding"""
        out = []
        row_count, columns_count = len(matrix), len(matrix[0])
        required_size = row_count * columns_count

        i, j = 0, 0
        while len(out) != required_size - 1:

            while j + 1 != columns_count and matrix[i][j + 1] is not None:
                out.append(matrix[i][j])
                matrix[i][j] = None
                j += 1

            while i + 1 != row_count and matrix[i + 1][j] is not None:
                out.append(matrix[i][j])
                matrix[i][j] = None
                i += 1

            while j - 1 != -1 and matrix[i][j - 1] is not None:
                out.append(matrix[i][j])
                matrix[i][j] = None
                j -= 1

            while i - 1 != -1 and matrix[i - 1][j] is not None:
                out.append(matrix[i][j])
                matrix[i][j] = None
                i -= 1

        out.append(matrix[i][j])
        return out


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """using the list of coordinates of the visited peaks"""
        out = []
        row_count, columns_count = len(matrix), len(matrix[0])
        required_size = row_count * columns_count
        visited = set()

        i, j = 0, 0
        while len(out) != required_size - 1:

            while j + 1 != columns_count and (i, j + 1) not in visited:
                out.append(matrix[i][j])
                visited.add((i, j))
                j += 1

            while i + 1 != row_count and (i + 1, j) not in visited:
                out.append(matrix[i][j])
                visited.add((i, j))
                i += 1

            while j - 1 != -1 and (i, j - 1) not in visited:
                out.append(matrix[i][j])
                visited.add((i, j))
                j -= 1

            while i - 1 != -1 and (i - 1, j) not in visited:
                out.append(matrix[i][j])
                visited.add((i, j))
                i -= 1

        out.append(matrix[i][j])
        return out
