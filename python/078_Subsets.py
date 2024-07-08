"""backtracking/recursion"""


class Solution(object):
    # backtracking
    # def subsets_bt(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     nums.sort()
    #     res = [[]]
    #     res.append(list(nums))
    #     self.counter_fred = 0
    #     for ls in range(1, len(nums)):
    #         self.get_subsets(res, nums, [], ls, 0)
    #     print(f'counter out: {self.counter_fred}')
    #     return res
    #
    # def get_subsets(self, res, nums, curr_set, ls, index):
    #     self.counter_fred += 1
    #     # recursive
    #     if ls == 0:
    #         res.append(list(curr_set))
    #     elif index < len(nums):
    #         curr_set.append(nums[index])
    #         self.get_subsets(res, nums, curr_set, ls - 1, index + 1)
    #         curr_set.pop()
    #         self.get_subsets(res, nums, curr_set, ls, index + 1)

    def subsets_bt(self, nums):
        result = []
        path = []
        self.counter = 0
        self.backtracking(nums, 0, path, result)
        print(self.counter)
        return result

    def backtracking(self, nums, startIndex, current_set, result):
        self.counter += 1
        result.append(current_set[:])  # 收集子集，要放在终止添加的上面，否则会漏掉自己
        # if startIndex >= len(nums):  # 终止条件可以不加
        #     return
        for i in range(startIndex, len(nums)):
            current_set.append(nums[i])
            self.backtracking(nums, i + 1, current_set, result)
            current_set.pop()  # backtracking, go on to explore other combination to form subset under current hierachy in the tree

    # def subsets(self, nums):
    #     # https://leetcode.com/discuss/89343/c-8-lines-bit-operation
    #     # doesn't work when len(nums) > 32
    #     nums.sort()
    #     res = []
    #     for i in range(1 << len(nums)):
    #         res.append(self.get_subsets(nums, i))
    #     return res
    #
    # def get_subsets(self, nums, magic):
    #     res = []
    #     for i in range(len(nums)):
    #         if (1 << i) & magic != 0:
    #            res.append(nums[i])
    #     return res

    def subsets(self, nums):
        # Sort and iteratively generate n subset with n-1 subset, O(n^2) and O(2^n)
        nums.sort()
        res = [[]]
        for index in range(len(nums)):
            size = len(res)
            # use existing subsets to generate new subsets
            for j in range(size):
                curr = list(res[j])
                curr.append(nums[index])
                res.append(curr)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsets_bt([1, 2, 3]))
