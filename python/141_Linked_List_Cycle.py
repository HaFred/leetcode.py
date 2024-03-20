# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     # Add max and check if reach max
    #     if head is None:
    #         return False
    #     count = 0
    #     max = 100000
    #     pos = head
    #     while pos is not None:
    #         count += 1
    #         pos = pos.next
    #         if count > max:
    #             return True
    #     return False

    # def hasCycle(self, head):
    #     # Hash or set
    #     dic = {}
    #     pos = head
    #     while pos is not None:
    #         try:
    #             dic[pos]
    #             return True
    #         except KeyError:
    #             dic[pos] = pos
    #         pos = pos.next
    #     return False

    def hasCycle(self, head):
        # Two points
        try:
            fast = head.next.next
            slow = head.next

            while fast != slow:
                fast = fast.next.next
                slow = slow.next
            return True
        except:  # means fast hits the end
            return False

    def hasCycle_dptr(self, head):
        if not head or not head.next:
            return False  # for null node or null next node, we can safely determine not cycled

        # Two points
        fast = head.next  # don't do too much linked, coz input may have only one node
        slow = head

        while fast != slow:
            if not fast or not fast.next:  # when fast reaches the end, and they're still not meeting, return False
                return False
            fast = fast.next.next
            slow = slow.next
        # out of loop means fast == slow
        return True


# indata = [3, 2, 0, -4]
# pos = 1
indata = [1]
pos = -1
outdata = 1
sol = Solution()
nodes = []
for i in range(len(indata)):
    nodes.append(ListNode(indata[i]))
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
# nodes[-1].next = nodes[pos] # make the cycle
out = sol.hasCycle(nodes[0])
print(out)
