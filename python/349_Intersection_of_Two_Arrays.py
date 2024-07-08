from collections import defaultdict

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # set
        return list(set(nums1) & set(nums2))



    def intersection_withdict(self, nums1, nums2):
        theset = defaultdict(int)
        res = []
        for i in nums1:
            if not theset.get(i):
                theset[i] = 1
        for i in nums2:
            if theset.get(i):
                res.append(i)
                theset[i] = 0  # rm as the problem requests
        return res


def getPlusSignCount(N, Len, Dir):
    x, y = 0, 0  # 初始位置
    up, down, left, right = set(), set(), set(), set()
    plus_signs = 0

    for L, D in zip(Len, Dir):
        if D == 'U':
            y_new = y + L
            for i in range(y, y_new):
                up.add(i)
            y = y_new
        elif D == 'D':
            y_new = y - L
            for i in range(y, y_new, -1):
                down.add(i)
            y = y_new
        elif D == 'L':
            x_new = x - L
            for i in range(x, x_new, -1):
                left.add(i)
            x = x_new
        elif D == 'R':
            x_new = x + L
            for i in range(x, x_new):
                right.add(i)
            x = x_new

            # 检查当前位置是否形成加号
        if x in left and x in right and y in up and y in down:
            plus_signs += 1

    return plus_signs