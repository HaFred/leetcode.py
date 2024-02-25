# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def remove_elements_iterative(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # add a extra head for removing head
        prehead = ListNode(-1)  # dummy before this head otherwise cannot analyze the first one
        prehead.next = head
        raw_prehead = prehead
        while head is not None:
            if head.val == val:
                prehead.next = head.next  # remove the ele that is in condition
            else:
                prehead = head
            head = head.next
        return raw_prehead.next  # the head of

    def rmi(self, head, val):
        calculating_node = ListNode(-1)  # initialized it as a prehead, such that the head of the ListNode can be considerred
        calculating_node.next = head
        prehead = calculating_node
        while calculating_node.next is not None:
            if calculating_node.next.val == val:
                calculating_node.next = calculating_node.next.next  # remove
            else:
                calculating_node = calculating_node.next
        return prehead.next

    def remove_elements_recursive(self, head, val):
        if head is None:
            return head
        head.next = self.remove_elements_recursive(head.next, val)
        if head.val == val:
            return head.next # return the ListNode for the linkage to the previous ListNode
        else:
            return head  # is not val, current head will be linked to the prev node


# below two funcs are all for feeding test data correctly and arange the output in list correctly, from `q328 odd even linked list`
def create_linked_list(arr):
    dummy = ListNode(-1)
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



input_arr = [1, 2, 6, 3, 4, 5, 6]
val = 6
linked_list_head = create_linked_list(input_arr)
sol = Solution()

# new_head = sol.remove_elements_iterative(linked_list_head, val)
# new_head = sol.rmi(linked_list_head, val)
new_head = sol.remove_elements_recursive(linked_list_head, val)

result = linked_list_to_list(new_head)
print(result)
# solution = Solution().removeElements_iterative(head, val)
# print(solution)
