import unittest

class Solution(object):
    """
    xx
    """
    # def binarySearch(self, nums, start, target):
    #     left, right = start, len(nums) - 1
    #     while left < right:
    #         mid = (left + right + 1) / 2
    #         if nums[mid] < target:
    #             # left should always less than target
    #             left = mid
    #         else:
    #             right = mid - 1
    #     return left


    # dichotomy
    def search(self, nums, target):
        """
        xx
        """
        if nums == []:
            return -1
        idx = 0
        # # take this out, avoid inf loop
        # if len(nums) == 1:
        #     return idx
        while len(nums)>=1:
            mid_idx = len(nums)//2
            if mid_idx > 0:
                mid = nums[mid_idx]
                if mid == target:
                    return len(nums)//2 + idx
                elif mid > target:
                    nums = nums[:len(nums)//2]
                elif mid < target:
                    idx += len(nums)//2
                    nums = nums[len(nums)//2:]
                else:
                    raise ValueError("Unexpected case")
            else:
                if nums[0] == target:
                    return idx
                else:
                    return -1
        # if go through the loop haven't return, then means no target found
        return -1


class Test(unittest.TestCase):
    """
    unittest
    """
    test_cases = [
        [2, 5],
        2,
        [5],
        5,
        [-1,0,3,5,9,12],
        9,
        [-1,0,3,5,9,12],
        2
        ]
    test_output = [0, 0, 4, -1]
    test_functions = [Solution().search]

    def test_search(self):
        """
        binary search
        """
        for i in range(int(len(self.test_cases)/2)):
            nums, target = self.test_cases[2*i], self.test_cases[2*i+1]
            for test_func in self.test_functions:
                test_result = test_func(nums, target)
                print(test_result)
                self.assertEqual(test_result, self.test_output[i])

if __name__ == '__main__':
    unittest.main()
