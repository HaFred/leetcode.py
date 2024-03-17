class Solution:
    def sorted_withlib(self, nums):
        return sorted(x * x for x in nums)

    def sorted(self, nums):  # double ptr here
        l, r, o_ptr = 0, len(nums) - 1, len(nums) - 1
        out = [0] * len(nums)
        while l <= r:
            lq = nums[l] ** 2
            rq = nums[r] ** 2
            pre_max = max(lq, rq)
            out[o_ptr] = pre_max
            o_ptr -= 1
            if lq == pre_max:
                l += 1
            else:
                r -= 1
        return out


Input = [-4, -1, 0, 3, 10]
Outpu = [0, 1, 9, 16, 100]
s = Solution()
# otu = s.sorted_withlib(Input)
# print(otu)

out = s.sorted(Input)
print(out)
