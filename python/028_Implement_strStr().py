class Solution(object):
    # def strStr(self, haystack, needle):
    #     """
    #     :type haystack: str
    #     :type needle: str
    #     :rtype: int
    #     """
    #     lsh, lsn = len(haystack), len(needle)
    #     if lsn == 0:
    #         return 0
    #     pos, index = 0, 0
    #     while index <= lsh - lsn:
    #         if haystack[index] == needle[pos]:
    #             backup = index
    #             while index < lsh and pos < lsn and haystack[index] == needle[pos]:
    #                 pos += 1
    #                 index += 1
    #             if pos == len(needle):
    #                 return index - pos
    #             index = backup
    #         index += 1
    #         pos = 0
    #     return -1

    # def strStr(self, haystack, needle):
    #     lsh, lsn = len(haystack), len(needle)
    #     if lsn == 0:
    #         return 0
    #     pos, index = 0, 0
    #     while index <= lsh - lsn:
    #         if haystack[index] == needle[0]:
    #             # slice index:index + lsn
    #             if haystack[index:index + lsn] == needle:
    #                 return index
    #         index += 1
    #     return -1

    # KMP
    # https://discuss.leetcode.com/topic/3576/accepted-kmp-solution-in-java-for-reference/2
    def strStr(self, haystack, needle):
        lsh, lsn = len(haystack), len(needle)
        if lsn == 0:
            return 0
        next = self.makeNext(needle)
        i = j = 0
        while i < lsh:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == lsn:
                    return i - lsn
            if i < lsh and haystack[i] != needle[j]:
                j = next[j]
        return -1

    def makeNext(self, needle):
        ls = len(needle)
        next = [0] * ls
        next[0], i, j = -1, 0, -1
        while i < ls - 1:
            if j == -1 or needle[i] == needle[j]:
                next[i + 1] = j + 1
                if needle[i + 1] == needle[j + 1]:
                    next[i + 1] = next[j + 1]
                i += 1
                j += 1
            if needle[i] != needle[j]:
                j = next[j]
        return next

    def strstr(self, haystack, needle):
        lsh, lsn = len(haystack), len(needle)
        if lsn == 0:
            return 0
        for i in range(lsh - lsn + 1):
            if haystack[i:i + lsn] == needle:
                return i
        return -1

    def strstr_kmp(self, haystack, needle):
        lsh, lsn = len(haystack), len(needle)
        if lsn == 0:
            return 0
        next = self.makeNext(needle)
        i = j = 0
        while i < lsh:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == lsn:
                    return i - lsn
            if i < lsh and haystack[i] != needle[j]:
                j = next[j]
        return -1

    def detect_cycle_linked_list(self, head):
        if head is None:
            return False
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                out.append('FizzBuzz')
            elif i % 3 == 0:
                out.append('Fizz')
            elif i % 5 == 0:
                out.append('Buzz')
            else:
                out.append(str(i))
        return out

    def drawingEdge(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        for i in range(1, n + 1):
            if i == 1 or i == n:
                out.append('*' * n)
            else:
                out.append('*' + ' ' * (n - 2) + '*')
        return out

    def getMinOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.getMinOperations(n // 2)
        else:
            return 1 + min(self.getMinOperations(n - 1), self.getMinOperations(n + 1))

    def getMinOperations_dp(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = 1 + dp[i - 1]
            if i % 2 == 0:
                dp[i] = min(dp[i], 1 + dp[i // 2])
        return dp[n]

    def getMinOperations_dp2(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = 1 + dp[i - 1]
            if i % 2 == 0:
                dp[i] = min(dp[i], 1 + dp[i // 2])
            if i % 3 == 0:
                dp[i] = min(dp[i], 1 + dp[i // 3])
        return dp[n]

