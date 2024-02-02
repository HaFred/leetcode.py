"""DP session in the programming carl. #2."""


class Solution(object):
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     dp = [0] * (n + 1)
    #     dp[0] = 1
    #     dp[1] = 1
    #     for i in range(2, n + 1):
    #         dp[i] = dp[i - 2] + dp[i- 1]
    #     return dp[n]

    def climbStairs(self, n):
        if n <= 1:
            return 1
        dp = [1] * 2
        for i in range(2, n + 1):
            dp[1], dp[0] = dp[1] + dp[0], dp[1]
        return dp[1]

    def climb_stairs(self, n):
        """
        DP1. dp arr is the current idx's #different_methods
        DP2. state transferring: dp[i] = dp[i-1] + dp[i-2]
        DP3. init at the beginning is ok
        DP4. in each for loop, assign dp[i], with increasing i
        DP5. dp == [1, 1, 2, 3] or if just two ele dp == [1,2] when i==1
        """
        dp = [1] * 2  # for fibonacci just needs to maintain two ele in dp arr, this two init as 1 and 1 representing 0 and 1st step
        for i in range(n-1):
            dp[1], dp[0] = dp[0] + dp[1], dp[1]
        return dp[1]


    # C = {1: 1, 2: 2}
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n in Solution.C:
    #         return Solution.C[n]
    #     else:
    #         result = Solution.C.get(n - 1, self.climbStairs(n - 1)) + \
    #                  Solution.C.get(n - 2, self.climbStairs(n - 2))
    #         Solution.C[n] = result
    #         return result

if __name__ == '__main__':
    s = Solution()
    input = 2
    out = s.climb_stairs(input)
    print(out)

