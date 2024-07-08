from collections import defaultdict


class Solution(object):
    """log(n), base of 10 maybe"""
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # https://en.wikipedia.org/wiki/Happy_number
        seen_numbers = set()
        while n > 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = sum(map(lambda x: int(x) * int(x), list(str(n))))
        return n == 1

    def isHappy_dict(self, n):
        def squ(x: str):
            return int(x) ** 2

        seen = defaultdict(int)
        # seen = {}
        while n > 1 and n not in seen.keys():
            seen[n] += 1
            n = sum(map(squ, list(str(n))))
        return n == 1  # if n != 1, means that it's a looped and out of seen


sol = Solution()
out = sol.isHappy_dict(19)
print(out)
