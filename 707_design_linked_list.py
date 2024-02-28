class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class MyLinkedList:

    def __init__(self):
        # self.the_list = []
        self.dummy_head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        """Note that list (array) is not implemented as a Linked List on the hw for python, they have different time complexity for both insertion and query, see https://programmercarl.com/%E9%93%BE%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html. Thus, no List can be used in this func here."""
        # if self.the_list[index] is not None:
        #     return self.the_list[index]
        if index < 0 or index >= self.size:
            return -1

        ptr = -1
        current = self.dummy_head
        while ptr < index:
            current = current.next
            ptr += 1
        return current.val

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.dummy_head.next
        self.dummy_head.next = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head  # init current
        while current.next:  # is not none then in the while loop
            current = current.next  # only when the tail, out loop
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        current = self.dummy_head
        # todo using for loop is clearer
        for i in range(index):
            current = current.next  # sliding to the one that needs to add on
        current.next = ListNode(val, current.next)  # adding
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:  # if index larger or equal to the size, cannot delete thus return
            return None
        current = self.dummy_head
        for i in range(index):
            current = current.next  # slide
        current.next = current.next.next
        self.size -= 1


if __name__ == '__main__':
    input_func = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    input_value = [[], [1], [3], [1, 2], [1], [1], [1]]
    null = None
    gt = [null, null, null, null, 2, null, 3]
    # for func, val in zip(input_func, input_value):
    #     func = globals()[func]
    #     out = func(val)
    #     print(out)

    # obj = MyLinkedList()
    # obj.addAtHead(input_value[1][0])
    # obj.addAtTail(input_value[2][0])
    # obj.addAtIndex(input_value[3][0], input_value[3][1])
    # param_1 = obj.get(input_value[4][0])
    # print(param_1)
    # obj.deleteAtIndex(input_value[5][0])
    # param_2 = obj.get(input_value[6][0])
    # print(param_2)

    a = MyLinkedList()
    a.addAtIndex(0, 10)
    a.addAtIndex(0, 20)
    a.addAtIndex(1, 30)
    out1 = a.get(0)

    print(out1)
