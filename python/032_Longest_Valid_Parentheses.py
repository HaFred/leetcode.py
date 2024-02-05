import pdb


class Solution(object):
    # def longestValidParentheses(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     ls = len(s)
    #     start = [0] * (ls + 1)
    #     all = [0] * (ls + 1)
    #     for i in reversed(range(ls - 1)):
    #         if s[i] == '(':
    #             if s[i + 1] == ')':
    #                 start[i] = 2
    #             if start[i + 1] + i + 1 < ls and s[start[i + 1] + i + 1] == ')':
    #                 start[i] = 2 + start[i + 1]
    #             if start[start[i] + i] > 0:
    #                 start[i] += start[start[i] + i]
    #         all[i] = max(start[i], all[i + 1])
    #     return all[0]

    def longestValidParentheses(self, s):
        # https://leetcode.com/discuss/87988/my-easy-o-n-java-solution-with-explanation
        ls = len(s)
        stack = []
        data = [0] * ls
        for i in range(ls):
            curr = s[i]
            if curr == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    data[i] = 1
                    data[stack.pop(-1)] = 1
        tep, res = 0, 0
        for t in data:
            if t == 1:
                tep += 1
            else:
                res = max(tep, res)
                tep = 0
        return max(tep, res)

    def fred_brute_force(self, s):
        """tc: O(n^3)"""
        def is_valid(x):
            """A sub func to determine the current substr is valid for parenthesis construction or not,
            in outer descending iterations of substrings """
            stack = []
            for i in range(len(x)):
                if x[i] == '(':
                    stack.append('(')
                elif stack != [] and stack[-1] == '(':  # when x[i] == ')' and last ele is '(', it matches parenthesis
                    stack.pop()
                else:  # if stack[-1] == ')'
                    return False  # coz it's gonna be a parenthesis with a lonely ')' here
            return stack == []  # if there is remaining symbol in stacks meaning that current string contains invalid
            # ( or ), thus False. Only empty list true

        if len(s) < 2: return 0
        n = len(s)
        for i in range(n if n % 2 == 0 else n - 1, 0, -2):  # start, stop, step
            for j in range(n - i + 1):  # on the left hand side idx
                if is_valid(s[j:j + i]):
                    return i  # found the max valid substring
        return 0  # if fail to find valid, return 0

    def fred_dp(self, s):
        """ tc: O(n)
         dp1. it records the longest num of the str. init as n size
         dp2. state transferring:
            1. get in the loop
            IF str[i] == ')', and IF str[i-dp[i-1]-1] == '(',
            then it's a full parenthesis thus dp[i]=2;
            2. consider str[i-dp[i-1]-1:i] and aggregate (only IF this idx>=0). Now dp[i]=2 + dp[i-1];
            3. for str[0:i-dp[i-1]-1]. Now dp[i] = 2 + dp[i-1] + dp[i-dp[i-1]-2]
         """
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        for i in range(len(s)):
            if s[i] == ')' and s[i - dp[i - 1] - 1] == '(' and i - dp[i - 1] - 1 >= 0:
                dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]
        return max(dp)

    def fred_stack_list(self):
        current_len = 0
        max_len = 0
        stack = []  # storing the current idx that is not forming parenthesis
        pass


if __name__ == '__main__':
    s = Solution()
    # print s.longestValidParentheses(")(((((()())()()))()(()))(")
    # print(s.longestValidParentheses(')()())'))
    # print(s.fred_brute_force(')()())'))
    print(s.fred_dp(')()())'))
