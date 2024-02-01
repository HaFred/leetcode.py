"""DP session in the programming carl. #3."""


class Solution(object):
    def minCostClimbingStairs(self, cost: [int]) -> int:
        """
        dp1. dp arr is min cost of the current idx step
        dp2. dp[i] == min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]), as the question requires getting on top of the whole steps. THEREFORE dp table needs to be len(cost) + 1
        dp5. make sure what the dp table first 5 elements, what are they. And then can test it cost = [10,15,20], dp[-1] == min(10+20, 15) == 15
        """
        dp_arr = [0] * (len(cost)+1)  # init dp table
        # dp_arr[1] = cost[0]
        for i in range(2, len(cost)+1):  # only do len(cost) - 1 times, and start with the dp_arr[1]
            dp_arr[i] = min(dp_arr[i - 1] + cost[i - 1], dp_arr[i - 2] + cost[i - 2])
        return dp_arr[-1]


if __name__ == '__main__':
    s = Solution()
    # input = [10, 15, 20]
    input = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    out = s.minCostClimbingStairs(input)
    print(out)
