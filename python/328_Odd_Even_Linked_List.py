import unittest


# Definition for singly-linked list.
class ListNode(object):
    """ 
    dd
    """

    def __init__(self, x):
        self.val = x
        self.next = None  # for unknown next ptr, set it to None


# using LinkedList space complexity is O(1), fixed
# if using two list to hold odd and even, space complexity is O(n)
class Solution(object):
    """
    dd
    """

    def oddEvenList(self, head):
        """ Process the head of the target linked list
        :type head: ListNode, pointing to the head of the processed linked list
        :rtype: ListNode
        """
        odd = head
        if head is None:
            return None
        if head.next is None:
            return head
        even_head = even = head.next
        while odd.next is not None and even.next is not None:
            odd.next = even.next  # the new come even.next is a odd, so can be the odd next for the odd to be
            odd = odd.next  # update odd to be
            even.next = odd.next  # the new come odd.next is a even
            even = even.next  # update even
        odd.next = even_head  # end of the odd, link to the even head
        return head

    # def oddEvenList(self, head):
    #     # slicing
    #     if (head != None):
    #         x = []
    #     else:
    #         return []
    #     while (head.next != None):
    #         x.append(head.val)
    #         head = head.next
    #     x.append(head.val)
    #     return x[0::2] + x[1::2]


# below two funcs are all for feeding test data correctly and arange the output in list correctly
def create_linked_list(arr):
    dummy = ListNode(0)
    ptr = dummy
    for num in arr:
        ptr.next = ListNode(num)  # create linked node for each coming .next
        ptr = ptr.next
    return dummy.next


def linked_list_to_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


def test_example(arr, func):
    head = create_linked_list(arr)
    result = linked_list_to_list(func(head=head))
    return result


class Test(unittest.TestCase):
    """
    """
    test_cases = [
        ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4])
    ]
    test_listnode_cases = []
    test_functions = [Solution().oddEvenList]

    # def prepare_linked_list(self, items: list) -> ListNode | None:
    #     if not items:
    #         return None
    #     root = None
    #     last_node = None
    #     for ind, val in enumerate(items):
    #         if ind == 0:
    #             root = ListNode(val)  # root node
    #             last_node = root
    #         else:
    #             last_node.next = ListNode(val)
    #             last_node = last_node.next
    #     return root

    # in unittest, all func starts with "test" will be run by unittest.main(). Thus carefully choosing the name
    def test_oddeven_link(self):
        for (test_in, test_out) in self.test_cases:
            for func in self.test_functions:
                out = test_example(arr=test_in, func=func)
                print(f'out is {out}')
                assert (out == test_out), f"{func.__name__} fialed for val: {test_in}, as {out}"


if __name__ == "__main__":
    unittest.main()
