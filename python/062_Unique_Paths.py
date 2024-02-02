class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dmap = [[0] * n for _ in range(m)]
        for i in range(m):
            dmap[i][0] = 1
        for j in range(n):
            dmap[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                l = u = 0
                if i-1 >= 0:
                    u = dmap[i-1][j]
                if j-1>= 0:
                    l = dmap[i][j-1]
                dmap[i][j] = l + u
        return dmap[m-1][n-1]

    def fred(self, m, n):
        """dp week 2#1.
        dp1. dp arr is 2d, dp[i][j] means the i row and j col's #unique_path in this ele.
        dp2. dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp3. init at the beginning and dp[1][0], dp[0][1] = 1, 1. Not only that, the whole first row and first column needs to be init a 1.
        dp4. the for loop increasing i,j. Don't modify the very first one again so not range(m) but range(1, m)
        dp5. dp[1][1] = 2 using the transfer equation, makes sense.
        """
        dp = [[0] * n for _ in range(m)]  # list whose len==m, the row. Each ele is a row with n ele
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

s = Solution()
m, n = 3, 2
out = s.fred(m, n)
# out = s.uniquePaths(m, n)
print(out)
