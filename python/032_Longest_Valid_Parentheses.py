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
        def is_valid(x):
            """A sub func to determine the current substr is valid for parenthesis construction or not, in outer descending iterations of substrings"""
            stack = []
            for i in range(len(x)):
                if x[i] == '(':
                    stack.append('(')
                elif stack != [] and stack[-1] == '(':  # when x[i] == ')' and last ele is '(', it matches parenthesis
                    stack.pop()
                else:  # if stack[-1] == ')'
                    return False  # coz it's gonna be a parenthesis with a lonely ')' here
            return stack == []  # if there is remaining symbol in stacks meaning that current string contains invalid ( or ), thus False. Only empty list true

        if len(s) < 2: return 0
        n = len(s)
        for i in range(n if n%2==0 else n-1, 0, -2):  # start, stop, step
            for j in range(n-i+1): # on the left hand side idx
                if is_valid(s[j:j+i]):
                    return i  # found the max valid substring
        return 0 # if fail to find valid, return 0

if __name__ == '__main__':
    s = Solution()
    # print s.longestValidParentheses(")(((((()())()()))()(()))(")
    # print(s.longestValidParentheses(')()())'))
    print(s.fred_brute_force(')()())'))
