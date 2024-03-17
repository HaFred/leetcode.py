# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     # iteratively
    #     if head is None:
    #         return
    #     stack = []
    #     pos = start = head
    #     while pos is not None:
    #         stack.append(pos)
    #         pos = pos.next
    #     while len(stack) > 0:
    #         if len(stack) >= 2:
    #             stack[0].val, stack[-1].val = stack[-1].val, stack[0].val
    #             stack.pop(0)
    #             stack.pop()
    #         else:
    #             stack.pop()
    #     return head
    #
    # def reverseList(self, head):
    #     # recursively
    #     if head is None:
    #         return head
    #     stack = []
    #     pos = head
    #     while pos is not None:
    #         stack.append(pos)
    #         pos = pos.next
    #     pre_head = ListNode(-1)
    #     self.do_reverse(stack, pre_head)
    #     return pre_head.next
    #
    # def do_reverse(self, stack, curr_head):
    #     if len(stack) == 0:
    #         curr_head.next = None
    #         return
    #     node = stack.pop()
    #     curr_head.next = node
    #     curr_head = node
    #     self.do_reverse(stack, curr_head)

    # def reverseList(self, head):
    #     # simple iteratively without extra space
    #     prev, curr = None, head
    #     while curr is not None:
    #         next_temp = curr.next
    #         curr.next = prev
    #         # # below two lines can also been used in a recursion like below commented
    #         # def reverse(prev, curr):  # moving the ptrs once curr.next re-assigned
    #         # return reverse(curr, temp)
    #         prev = curr
    #         curr = next_temp
    #     return prev

    def reverseList(self, head):
        """ steps of doing recursion
        1. define end state and return
        2. determine where to recurse it in the function
        3. determine what is the return value for the recursion line
        4. determine the real func here that helps the recursion works
        """
        # recursion
        # simple recursively without extra space
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head  # the original next node (head.next) now has a new next, which is the prev one, thus reverse the linked list
        head.next = None  # delete the original direction of link
        return new_head  # return the new head of the Linked List

    def reverse_list_with_double_ptr(self, head):
        # iterative double ptr
        left_ptr, right_ptr = None, head
        while right_ptr:
            temp = right_ptr.next
            right_ptr.next = left_ptr  # change the link direction, from left to right to right to left
            # update the ptr position
            left_ptr = right_ptr
            right_ptr = temp

        return left_ptr  # right ptr already None when reaches here, left ptr is the new head



if __name__ == '__main__':
    from python.design_linked_list_707 import MyLinkedList
    input_head = [1, 2, 3, 4, 5]
    output_head = [5, 4, 3, 2, 1]
    test_node = ListNode(input_head[0])
    test_node.next = ListNode(input_head[1])
    input_linked_list = MyLinkedList()
    for i in range(len(input_head)):
        input_linked_list.addAtIndex(i, input_head[i])
    solution = Solution()
    # out = solution.reverseList(input_linked_list.dummy_head)
    out = solution.reverse_list_with_double_ptr(input_linked_list.dummy_head)
    for i in range(len(input_head)):
        val = out.val
        out = out.next
        print(val)
