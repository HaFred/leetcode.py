import unittest

""" The tree for this island problem is shown below: 
        r0c0
    r1c0    r1c1    r1c2
r2c0    r2c1    r2c2    r2c3


Therefore, for all the recursive way that exploring the neighbors, it is actually BFS;
For all the recursive way that exploring the row or the column first, it is actually DFS.
"""


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
        print('exploring [{},{}]'.format(i, j))
        # recursively explore all the neighbors, searching directions is its neighbors, thus BFS
        if i - 1 >= 0 and grid[i - 1][j] == '1':  # make sure inside bound and is land
            self.explore(grid, i - 1, j)
        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self.explore(grid, i, j - 1)
        if i + 1 < len(grid) and grid[i + 1][j] == '1':
            self.explore(grid, i + 1, j)
        if j + 1 < len(grid[i]) and grid[i][j + 1] == '1':
            self.explore(grid, i, j + 1)


class SolutionDFS(object):
    def numIslandsDFS(self, grid):
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
        print('exploring [{},{}]'.format(r, c))
        directions = [(0, 1), (0, -1), (1, 0), (-1,
                                                0)]  # this direction means that you traverse the row first, by keeping the row and change the col, thus this is a depth first search wrt the row
        for dr, dc in directions:  # explore all the neighbors
            self.explore(r + dr, c + dc, grid)


class Test(unittest.TestCase):
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    expected = 3
    test_funcs1 = [Solution().numIslands]
    test_funcs2 = [SolutionDFS().numIslandsDFS]
    test_funcs = test_funcs1 + test_funcs2

    def testNum(self):
        for test_func in self.test_funcs:
            print('doing {}'.format(test_func.__name__))
            self.assertEqual(test_func(self.grid), self.expected)
            # restore input
            self.grid = [["1", "1", "0", "0", "0"],
                         ["1", "1", "0", "0", "0"],
                         ["0", "0", "1", "0", "0"],
                         ["0", "0", "0", "1", "1"]]
