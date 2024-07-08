from typing import List, Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


import collections


class Solution(object):
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:  # new level for each iter
            level = []
            for i in range(len(queue)):
                node_proc = queue.popleft()
                level.append(node_proc.val)
                if node_proc.children:
                    for j in range(len(node_proc.children)):
                        queue.append(node_proc.children[j])
            result.append(level)
        return result


if __name__ == '__main__':
    root = Node(1)
    root.children = [Node(3), Node(2), Node(4)]
    root.children[0].children = [Node(5), Node(6)]
    print(Solution().levelOrder(root))
    # should expecting this
    # Input: root = [1, 3, 2, 4, 5, 6]
    # Output: [[1], [3, 2, 4], [5, 6]]
    # Explanation: The above tree is represented in the level order.
    # (1) -> 1
    # (2) -> 3, 2, 4
    # (3) -> 5, 6
    # return its level order traversal as:
    # [
    #     [1],
    #     [3, 2, 4],
    #     [5, 6]
    # ]
    #
    # Input: root = [1, null, 2, 3, 4, 5, null, null, 6, 7, null, 8, null, 9, 10]
    # Output: [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10]]
    # Explanation: The above tree is represented in the level order.
    # (1) -> 1
    # (2) -> 2
    # (3) -> 3, 4, 5
    # (4) -> 6, 7
    # (5) -> 8
    # (6) -> 9
    # (7) -> 10
    # return its level order traversal as:
    # [
    #     [1],
    #     [2],
    #     [3, 4, 5],
    #     [6, 7],
    #     [8],
    #     [9],
    #     [10]
    # ]
    #
    # Input: root = []
    # Output: []
    # Explanation: The tree has no nodes.
    # return [].
    #
    # Input: root = [1]
    # Output: [[1]]
    # Explanation: The tree has only one node.
    # return [[1]].
    #
