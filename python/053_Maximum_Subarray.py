"""This question is supposed to be a greedy problem. But it can be done with dp for sure."""


class Solution(object):
    # def maxSubArray(self, nums):
    #     return self.maxSubArrayHelper(nums, 0, len(nums) - 1)
    #
    # def maxSubArrayHelper(self, nums, l, r):
    #     if l > r:
    #         return -2147483647
    #     mid = (l + r) / 2
    #     leftAns = self.maxSubArrayHelper(nums, l, mid - 1)
    #     rightAns = self.maxSubArrayHelper(nums, mid + 1, r)
    #     lMaxSum = res = 0
    #     for i in range(mid - 1, l -1, -1):
    #         res += nums[i]
    #         lMaxSum = max(res, lMaxSum)
    #     rMaxSum = res = 0
    #     for i in range(mid + 1, r + 1):
    #         res += nums[i]
    #         rMaxSum = max(res, rMaxSum)
    #     return max(lMaxSum + nums[mid] + rMaxSum, max(leftAns, rightAns))

    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     ls = len(nums)
    #     start = [0] * ls
    #     all = [0] * ls
    #     start[-1], all[-1] = nums[-1], nums[-1]
    #     for i in reversed(range(ls - 1)):
    #         start[i] = max(nums[i], nums[i] + start[i + 1])
    #         all[i] = max(start[i], all[i + 1])
    #     return all[0]

    # def maxSubArray(self, nums):
    #     ls = len(nums)
    #     start, all = nums[-1], nums[-1]
    #     for i in reversed(range(ls - 1)):
    #         start = max(nums[i], nums[i] + start)
    #         all = max(start, all)
    #     return all

    def maxSubArray(self, nums):
        maxEndingHere = maxSofFar = nums[0]
        for i in range(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i])
            maxSofFar = max(maxEndingHere, maxSofFar)
        return maxSofFar

    def max_sub_dp(self, nums):
        """
        dp1: dp arr stores the max sum of its subarray
        dp2: dp[i]=max(dp[i]-1 + num[i], num[i]). But the result is not the final dp arr, but the max(dp).
        dp3: dp[0]=num[0], needs to init len(nums) space for dp arr
        dp4: for loop starts with dp[1], and increasing
        dp5: when nums = [5,4,-1,7,8], the elements sum are all positive therefore can be all
        """
        dp = [0] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = Solution()
out = s.max_sub_dp(nums)
print(out)
