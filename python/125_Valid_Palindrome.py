import unittest

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alnum_s = [t.lower() for t in s if t.isalnum()]  # make all lower case
        ls = len(alnum_s)
        if ls <= 1:
            return True
        mid = ls / 2
        for i in range(int(mid)):
            if alnum_s[i] != alnum_s[ls - 1 - i]:  # check if palindrome
                return False
        return True


class Test(unittest.TestCase):
    """dd """
    test_cases = [
         "A man, a plan, a canal: Panama",
         "race a car",
         ""
    ]
    test_results = [
        True,
        False,
        True
    ]
    def test_example(self):
        func = Solution().isPalindrome
        for i, input in enumerate(self.test_cases):
            # actual = test_example(arr, func)
            # self.assertEqual(actual, expected)
            # input = self.test_cases[i]
            output = self.test_results[i]
            out = func(input)
            print(out)
            assert out == output, f"Wrong: {out} != {output}"


if __name__ == "__main__":
    unittest.main()
