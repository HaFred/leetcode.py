# not dp, but using binary as the question is all about binary operations.
class Solution:
    def minOperations(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n < 0:
            return 0

        # do comparison with either makes up with 1 or not
        ret = 0
        # pos int n means it is single precision
        for i in range(32):
            if self.count_1(n + (1 << i)) + 1 <= self.count_1(n):  # in fact, it considers the case of subtraction, coz if it is 0b'10000000001, apparently it won't get into the loop, and the result will just ret + self.count_1(n), which is done by doing substation
                n += 1 << i
                ret += 1
        return ret + self.count_1(n)

    def count_1(self, n):
        binary_n = bin(n)
        return binary_n.count('1')


# indata = [3, 2, 0, -4]
# pos = 1
# indata = 39
# output = 3
indata = 54
output = 3
sol = Solution()
out = sol.minOperations(indata)
print(out)
