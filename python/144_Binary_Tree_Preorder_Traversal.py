# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # def __init__(self):
    #     self.result = []
    #
    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if root is None:
    #         return []
    #     self.preorderTraversalHelper(root)
    #     return self.result
    #
    # def preorderTraversalHelper(self, node):
    #     if node is None:
    #         return
    #     self.result.append(node.val)
    #     self.preorderTraversalHelper(node.left)
    #     self.preorderTraversalHelper(node.right)

    def preorderTraversal_prev(self, root: [TreeNode]):
        # stack
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        self.fred_preorder_traversal_func(root)

    def fred_preorder_traversal_func(self, node, stack):
        """
        binary tree (bt) traversal steps:
        bt1: determine the traverse param: which is the current handling node and the global preorder node list
        bt2: determine end condition: when it reaches null ptr, ends for this traverse iteration (here formally speaking is using recursion)
        bt3: since it is preorder, takes middle-left-right
        """
        if node == null: return
        stack.append(node.val)  # middle
        self.fred_preorder_traversal_func(node.left, stack)  # left
        self.fred_preorder_traversal_func(node.right.stack)


input = [1, null, 2, 3]


# for linked list or binary tree questions, if input is a list, then it needs to be adapted first before passed into the solution function
def create_linked_list(arr):
    dummy = TreeNode(0)
    ptr = dummy
    for num in arr:
        ptr.next = TreeNode(num)  # create linked node for each coming .next
        ptr = ptr.next
    return dummy.next
