# Definition for a binary tree node.
from typing import List, Optional
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution(object):
    # def levelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     if root is None:
    #         return []
    #     self.get_level(res, root, 0)
    #     return res
    #
    # def get_level(self, res, root, depth):
    #     if root is None:
    #         return
    #     if depth == len(res):
    #         res.append([])
    #     res[depth].append(root.val)
    #     self.get_level(res, root.left, depth + 1)
    #     self.get_level(res, root.right, depth + 1)

    def levelOrder(self, root):
        # https://leetcode.com/discuss/90680/9-lines-python-code
        if root is None:
            return []
        q = [[root]]
        for level in q:
            record = []
            for node in level:
                if node.left:
                    record.append(node.left)
                if node.right:
                    record.append(node.right)
            if record:
                q.append(record)
        return [[x.val for x in level] for level in q]

    def levelOrderToTest(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result

    def levelOrderFredRe(self, root):
        if not root:
            return []
        queue = collections.deque([root])  # store current level of tree's nodes
        result = []
        while queue:
            level_of_tree = []
            for i in range(len(queue)):
                node_to_proc = queue.popleft()
                level_of_tree.append(node_to_proc.val)
                if node_to_proc.left:
                    queue.append(node_to_proc.left)  # push from the right
                if node_to_proc.right:
                    queue.append(node_to_proc.right)
            result.append(level_of_tree)
        return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrder(root))
    print(Solution().levelOrderToTest(root))
    print(Solution().levelOrderFredRe(root))
    # should expecting this
    # Input: root = [3, 9, 20, null, null, 15, 7]
    # Output: [[3], [9, 20], [15, 7]]

    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # print(Solution().levelOrder(root))
    # print(Solution().levelOrderToTest(root))
