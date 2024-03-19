# class Solution(object):
#     def isValid(self, s):

#
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
        stack = []
        for t in s:
            if t == ')':
                try:
                    current = stack.pop()
                    if current != '(':
                        return False
                except:
                    return False
            elif t == '}':
                try:
                    current = stack.pop()
                    if current != '{':
                        return False
                except:
                    return False
            elif t == ']':
                try:
                    current = stack.pop()
                    if current != '[':
                        return False
                except:
                    return False
            else:
                stack.append(t)
        if len(stack) == 0:
            return True
        else:
            return False

    def isValid_stack(self, s):
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                out_stack = stack.pop()
                if not ((out_stack == '(' and i == ')') or \
                        (out_stack == '[' and i == ']') or \
                        (out_stack == '{' and i == '}')):
                    return False
        if len(stack) != 0:  # make sure it is not single side column
            return False
        else:
            return True

    # def isValid(self, s):
    #     # python replace
    #     n = len(s)
    #     if n == 0:
    #         return True
    #
    #     if n % 2 != 0:
    #         return False
    #
    #     while '()' in s or '{}' in s or '[]' in s:
    #         s = s.replace('{}', '').replace('()', '').replace('[]', '')
    #
    #     if s == '':
    #         return True
    #     else:
    #         return False


if __name__ == '__main__':
    sinput = "()[]{}"
    gt = True
    s = Solution()
    out = s.isValid_stack(sinput)
    print(out)
