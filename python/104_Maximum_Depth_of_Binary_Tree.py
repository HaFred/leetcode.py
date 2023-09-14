# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import unittest

# # recursive DFS, t: O(n), s: O(n), where n is the number of nodes in the tree
# # big O upper bound, t is O(n) for the unbalanced tree
# class Solution:
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None:
#             return 0
#         ld = self.maxDepth(root.left)
#         rd = self.maxDepth(root.right)
#         return 1 + max(ld, rd)

# # iterative DFS, emulate the stack, same big O
# class Solution:
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         stack = []
#         depth = 0
#         if root is not None:
#             stack.append((1, root))
#         while stack != []:
#             cur_depth, root = stack.pop()  # pop out each branch as it is just pushed in, thus DFS
#             if root is not None:
#                 depth = max(depth, cur_depth)  # update depth val in the as the max
#                 stack.append((cur_depth + 1, root.left))  # push the updated-depth-node pair into the stack
#                 stack.append((cur_depth + 1, root.right))
#         return depth
    

# iterative BFS, need a FIFO to do the breadth, thus queue
# can also do a deque version as in https://github.com/neetcode-gh/leetcode/blob/ec5ef95c2d42eca117a854d070fa122649f2647a/python/0104-maximum-depth-of-binary-tree.py#L27
class Solution:
    def maxDepth(self, root):
        queue = []
        depth = 0
        if root is not None:
            queue.append((1, root))
        while queue != []:
            cur_depth, root = queue.pop(0)
            if root is not None:  # if root is None, meaning that there is no children node, thus depth should not be updated with the below line
                depth = max(depth, cur_depth)
                queue.append((cur_depth +1, root.left))
                queue.append((cur_depth +1, root.right))
        return depth
    
def create_binary_tree(arr):
    """
    :type arr: list
    :rtype: TreeNode
    """
    if arr == []:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


class Test(unittest.TestCase):
    null = None
    input_list = [3,9,20,null,null,15,7]
    output_list = 3

    def test_example(self):
        root = create_binary_tree(self.input_list)
        output = Solution().maxDepth(root)
        self.assertEqual(output, self.output_list)


if __name__ == '__main__':
    unittest.main()
