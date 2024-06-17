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
