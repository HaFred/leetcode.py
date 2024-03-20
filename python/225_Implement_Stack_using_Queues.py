# class Stack(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.queue1 = []
#         self.queue2 = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: nothing
#         """
#         self.queue1.append(x)
#
#     def pop(self):
#         """
#         :rtype: nothing
#         """
#         while len(self.queue1) > 1:
#             curr = self.queue1.pop(0)
#             self.queue2.append(curr)
#         if len(self.queue1) == 1:
#             self.queue1.pop(0)
#         while len(self.queue2):
#             curr = self.queue2.pop(0)
#             self.queue1.append(curr)
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         while len(self.queue1) > 1:
#             curr = self.queue1.pop(0)
#             self.queue2.append(curr)
#         return self.queue1[0]
#
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return len(self.queue1) + len(self.queue2) == 0


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.curr_top = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue2.append(x)
        self.curr_top = x
        while len(self.queue1):
            self.queue2.append(self.queue1.pop(0))
        temp = self.queue2
        self.queue2 = self.queue1
        self.queue1 = temp

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue1.pop(0)
        if len(self.queue1):
            self.curr_top = self.queue1[0]

    def top(self):
        """
        :rtype: int
        """
        if self.empty() is False:
            return self.curr_top

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1) == 0


# todo notice that another method in python is to use deque
class MyStack:

    def __init__(self):
        self.queue = []
        self.current_top = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.current_top = x

    def pop(self, *a) -> int:
        if len(self.queue) == 0:
            return None
        qsize = len(self.queue)
        while qsize > 1:
            self.queue.append(self.queue[0])
            self.queue.pop(0)
            qsize -= 1
        result = self.queue.pop(0)
        if self.empty():
            self.current_top = 0
        else:
            self.current_top = self.queue[-1]
        return result

    def top(self, *a) -> int:
        if self.empty() is False:
            return self.current_top

    def empty(self, *a) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
# obj.push(1)
# obj.push(2)
# param_2 = obj.pop()
# # param_3 = obj.top()
# param_4 = obj.empty()
# print(param_4)

# Input = ["push", "push", "pop", "top"]
# Input2 = [[1], [2], [], []]
Input = ["push", "push", "push", "top", "pop", "top", "pop", "top", "empty", "pop", "empty"]
Input2 = [[1], [2], [3], [], [], [], [], [], [], [], []]

for func, var in zip(Input, Input2):
    fun = getattr(obj, func)
    p = fun(var)
    print(p)
