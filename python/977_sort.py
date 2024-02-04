class Solution:
    def sorted(self, nums):
        return sorted(x * x for x in nums)


Input = [-4, -1, 0, 3, 10]
Outpu = [0, 1, 9, 16, 100]
s = Solution()
otu = s.sorted(Input)
print(otu)
