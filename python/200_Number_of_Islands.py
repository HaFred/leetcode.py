import unittest


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # BFS with marks
        if grid is None or len(grid) == 0:
            return 0
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):  # explore each row, each col
                if grid[i][j] == '1':
                    self.explore(grid, i, j)
                    islands += 1
        return islands

    def explore(self, grid, i, j):
        grid[i][j] = 'X'  # make explored as 'X', then won't be explore by '1' again
        # recursively explore all the neighbors
        if i - 1 >= 0 and grid[i - 1][j] == '1':
            self.explore(grid, i - 1, j)
        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self.explore(grid, i, j - 1)
        if i + 1 < len(grid) and grid[i + 1][j] == '1':
            self.explore(grid, i + 1, j)
        if j + 1 < len(grid[i]) and grid[i][j + 1] == '1':
            self.explore(grid, i, j + 1)


class SolutionDFS(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # DFS with marks
        if grid is None or len(grid) == 0:
            return 0
        islands = 0
        self.visited = set()
        self.rows, self.cols = len(grid), len(grid[0])
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == "1" and (r, c) not in self.visited:
                    self.explore(r, c, grid)
                    islands += 1
        return islands

    def explore(self, r, c, grid):
        if r not in range(self.rows) or c not in range(self.cols) or grid[r][c] == "0" or (r, c) in self.visited:
            return
        self.visited.add((r, c))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:  # explore all the neighbors
            self.explore(r + dr, c + dc, grid)


class Test(unittest.TestCase):
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    expected = 3
    test_funcs1 = [Solution().numIslands]
    test_funcs2 = [SolutionDFS().numIslands]
    test_funcs = test_funcs1 + test_funcs2

    def testNum(self):
        for test_func in self.test_funcs:
            self.assertEqual(test_func(self.grid), self.expected)
            # restore input
            self.grid = [["1", "1", "0", "0", "0"],
                         ["1", "1", "0", "0", "0"],
                         ["0", "0", "1", "0", "0"],
                         ["0", "0", "0", "1", "1"]]
