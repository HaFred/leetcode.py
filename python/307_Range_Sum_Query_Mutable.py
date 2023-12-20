import math
import unittest


# Time Limit Exceeded for the naive solution
class NumArray:

    def __init__(self, nums):
        self.num_list = nums

    def update(self, index: int, val: int) -> None:
        self.num_list[index] = val

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += self.num_list[i]

        return sum


# with segment tree
class Node(object):
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum
        self.left = None
        self.right = None


class myNumArr(object):
    def __init__(self, nums):
        self.nums = []
        self.ls = len(nums)
        self.b = []

        def createTree(nums, start, end):
            if start > end:
                return None
            if start == end:
                node = Node(start, end, nums[start])
                return node
            mid = (start + end) // 2
            node = Node(start, end, 0)
            node.left = createTree(nums, start, mid)
            node.right = createTree(nums, mid + 1, end)
            node.sum = node.left.sum + node.right.sum
            return node

        self.root = createTree(nums, 0, self.ls - 1)

    def update(self, i, val):
        def updateVal(root, i, val):
            if root.start == root.end:
                root.sum = val
                return val
            mid = (root.start + root.end) // 2
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            root.sum = root.left.sum + root.right.sum
            return root.sum
        return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.sum
            mid = (root.start + root.end) // 2
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i > mid:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)

        return rangeSum(self.root, i, j)

# class NumArray(object):
#     def __init__(self, nums):
#         """
#         initialize your data structure here.
#         :type nums: List[int]
#         """
#         self.nums = list(nums)
#         ls = len(nums)
#         self.ls = int(math.ceil(math.sqrt(ls)))
#         self.b = [0] * self.ls
#         for i in range(ls):
#             self.b[i / self.ls] += nums[i]
#
#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: int
#         """
#         b_l = i / self.ls
#         self.b[b_l] = self.b[b_l] - self.nums[i] + val
#         self.nums[i] = val
#
#     def sumRange(self, i, j):
#         """
#         sum of elements nums[i..j], inclusive.
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         res = 0
#         startBlock = i / self.ls
#         endBlock = j / self.ls
#         if startBlock == endBlock:
#             res = sum(self.nums[i:j + 1])
#         else:
#             res += sum(self.nums[i:(startBlock + 1) * self.ls])
#             res += sum(self.b[startBlock + 1: endBlock])
#             res += sum(self.nums[endBlock * self.ls:j + 1])
#         return res


# class NumArray(object):
#     def __init__(self, nums):
#         """
#         initialize your data structure here.
#         :type nums: List[int]
#         """
#         self.ls = len(nums)
#         self.tree = [0] * (self.ls * 2)
#         self.buildTree(nums)
#
#     def buildTree(self, nums):
#         i, j = self.ls, 0
#         while i < 2 * self.ls:
#             self.tree[i] = nums[j]
#             i += 1
#             j += 1
#         for i in reversed(range(1, self.ls)):
#             self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
#
#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: int
#         """
#         i += self.ls
#         self.tree[i] = val
#         while i > 0:
#             left = right = i
#             if i % 2 == 0:
#                 right = i + 1
#             else:
#                 left = i - 1
#             self.tree[i / 2] = self.tree[left] + self.tree[right]
#             i /= 2
#
#     def sumRange(self, i, j):
#         """
#         sum of elements nums[i..j], inclusive.
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         res = 0
#         i += self.ls
#         j += self.ls
#
#         while i <= j:
#             if i % 2 == 1:
#                 res += self.tree[i]
#                 i += 1
#             if j % 2 == 0:
#                 res += self.tree[j]
#                 j -= 1
#             i /= 2
#             j /= 2
#         return res
#
#         # Your NumArray object will be instantiated and called as such:
#         # numArray = NumArray(nums)
#         # numArray.sumRange(0, 1)
#         # numArray.update(1, 10)
#         # numArray.sumRange(1, 2)


class TestSolution(unittest.TestCase):
    def test_update(self):
        numArray = myNumArr([1, 3, 5])
        numArray.update(1, 2)
        self.assertEqual(numArray.sumRange(0, 2), 8)
        numArray.update(0, 3)
        self.assertEqual(numArray.sumRange(0, 2), 10)
