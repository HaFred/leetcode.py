import unittest


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int

        1. DP
        2. DFS
        """
        # check
        if dungeon is None or len(dungeon) == 0:
            return 0

        # init
        rows, cols = len(dungeon), len(dungeon[0])
        # # allocate mem to dp
        # dp = [[0] * cols for _ in range(rows)]
        # or simply
        dp = [0] * cols * rows
        # handle the lower right corner cases
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        # handle the last row, and the last col
        for j in range(cols - 2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j+1] - dungeon[-1][j])
        for i in range(rows - 2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1] - dungeon[i][-1])

        for i in range(rows - 2, -1, -1):  # the for loop already handle in dp fashion
            for j in range(cols - 2, -1, -1):
                dp[i][j] = min(max(1, dp[i+1][j] - dungeon[i][j]), max(1, dp[i][j+1] - dungeon[i][j]))
        print('dp00 is {}'.format(dp[0][0]))
        return dp[0][0]


class Test(unittest.TestCase):
    def test1(self):
        dungeon = [[-2, -3, 3],
                   [-5, -10, 1],
                   [10, 30, -5]]
        expected = 7
        sol = Solution()
        self.assertEqual(sol.calculateMinimumHP(dungeon), expected)
