"""
for hash table questions, there are two types:
1. use {}/defaultdict (the latter gives non-key-existent val as 0) to record those whose key are text str;
2. use set() or array [] to encode those of the same type, such as uncounted integers (as keys).
"""
from typing import List


class Solution(object):
    # def threeSum(self, nums):
    #     # skip duplicate
    #     # O(n^3)
    #     if len(nums) < 3:
    #         return []
    #     nums.sort()
    #     ls = len(nums)
    #     result = []
    #     for i in range(0, ls - 2):
    #         if nums[i] > 0:
    #             break
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         j = i + 1
    #         k = ls - 1
    #         while(j < k):
    #             temp = [nums[i], nums[j], nums[k]]
    #             s = sum(temp)
    #             jtemp = nums[j]
    #             ktemp = nums[k]
    #             if s <= 0:
    #                 j += 1
    #                 while(j < k and jtemp == nums[j]):
    #                     j += 1
    #                 if s == 0:
    #                     result.append(temp)
    #             else:
    #                 k -= 1
    #                 while(j < k and ktemp == nums[k]):
    #                     k -= 1
    #     return result
    # def threeSum(self, nums):
    #     """
    #         :type nums: List[int]
    #         :rtype: List[List[int]]
    #     """
    #     # using multiple 2 sum
    #     nums.sort()
    #     result, visited = set(), {}
    #     for i in xrange(len(nums) - 2):
    #         table, target = {}, -nums[i]
    #         if nums[i] not in visited:
    #             for j in xrange(i + 1, len(nums)):
    #                 if nums[j] not in table:
    #                     table[target - nums[j]] = j
    #                 else:
    #                     result.add((nums[i], target - nums[j], nums[j]))
    #             visited[nums[i]] = 1
    #     return list(result)

    def threeSum(self, nums):
        res = []
        nums.sort()
        ls = len(nums)
        for i in range(ls - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = ls - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif curr < 0:
                    j += 1
                else:
                    k -= 1
        return res

    def threeSum_db_ptr(self, nums: List[int]) -> List[List[int]]:
        """we maintain the three num in the list as [x, left, right] after sorting, such that the condition satisfies."""
        results = []
        nums.sort()  # sorting is primarily under o(n^2), while the algo 3sum here is o(n^2) as well thus no influence if we do the sorting here
        for i in range(len(nums)):
            if nums[i] > 0:
                return results  # now with ptr mv, sum is already larger than 0, return what in results

            if i > 0 and nums[i] == nums[
                i - 1]:  # will form an exact same pair with the prev, coz only i update here neither left nor right updated
                continue

            # init
            left = i + 1
            right = len(nums) - 1  # the last one ptr

            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                if _sum < 0:
                    left += 1
                elif _sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    # at least one time even not equal to keep moving
                    right -= 1
                    left += 1

        return results

    def threeSum_dict(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                return res  # now with ptr mv, sum is already larger than 0, return what in results
            if i > 0 and nums[i-1] == nums[i]:
                continue
            dict_for_c = {}
            for j in range(i + 1, len(nums)):
                dict_for_c




if __name__ == '__main__':
    nums = [0, 0, 0]
    s = Solution()
    out = s.threeSum_db_ptr(nums)
    print(out)
