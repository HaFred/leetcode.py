from collections import defaultdict

class Solution(object):
    # def isAnagram(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     # sort
    #     return sorted(s) == sorted(t)

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # hash
        # https://leetcode.com/articles/valid-anagram/
        if len(s) != len(t):
            return False
        counter = [0] * 26  # an arr counter for char
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        for num in counter:
            if num != 0:
                return False
        return True

    def isAnagram_defaultdict(self, s, t):
        if len(s) != len(t):
            return False
        counter = defaultdict(int)  # needs to make the default val of the dict as int 0, using dict seems not able to meet this
        # counter = {}
        for char in s:
            counter[char] += 1
        for char in t:
            counter[char] -= 1
        for k, v in counter.items():
            if v != 0:
                return False
        return True


sol = Solution()
s = "anagram"
t = "nagaram"
out = sol.isAnagram_defaultdict(s, t)
print(out)
