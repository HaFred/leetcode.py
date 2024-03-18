# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """

"""fred: below try the double ptr method"""


class SolutionFred(object):
    def removeElement_index_count_unordered(self, nums, val):
        ls = len(nums)
        if ls == 0:
            return ls
        count = 0
        index = 0
        while index < ls - count:  # fast ptr index: if not reaching the end, then in loop
            if nums[index] == val:
                # changing the order of ele by assigning the last ele to the current index. And the index is not added up until num[index] != val, to make sure that every time bring back the last index iis not val
                nums[index] = nums[ls - 1 - count]
                count += 1
            else:
                index += 1
        return ls - count

    # def removeElement_db_ptr(self, nums, val):
    #     ls = len(nums)
    #     if ls == 0:
    #         return ls
    #     fast, slow = 0, 0
    #     while fast < ls:
    #         if nums[fast] != val:
    #             nums[slow] = nums[fast]
    #             slow += 1
    #         fast += 1
    #     return slow

    def removeElement_db_ptr(self, nums, val):
        ls = len(nums)
        if ls == 0:
            return ls
        fast, slow = 0, 0
        while fast < ls:  # out of loop when fast == ls, reach idx range
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


class Solution(object):
    # def removeElement(self, nums, val):
    #     ls = len(nums)
    #     if ls == 0:
    #         return ls
    #     pos = 0
    #     for i in range(ls):
    #         if nums[i] == val:
    #             continue
    #         else:
    #             nums[pos] = nums[i]
    #             pos += 1
    #     # del nums[pos:]
    #     return pos

    def removeElement(self, nums, val):
        ls = len(nums)
        if ls == 0:
            return ls
        count = 0
        index = 0
        while index < ls - count:
            if nums[index] == val:
                nums[index] = nums[ls - 1 - count]
                count += 1
            else:
                index += 1
        return ls - count


if __name__ == '__main__':
    # begin
    # s = Solution()
    # print(s.removeElement([1], 1))

    s2 = SolutionFred()
    nums = [3, 2, 2, 3]
    # k = s2.removeElement_index_count_unordered(nums, 3)
    k = s2.removeElement_db_ptr(nums, 3)
    print(f"k is {k}, nums is {nums}")
