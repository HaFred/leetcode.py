# time com: O(n)
# space com: O(1)

class Solution:
    def findMajority(self, input):
        count = 0
        candidate = None  # by doing one buffer only, the space complexity is O(1)
        for num in input:
            if count == 0:
                candidate = num
            if num == candidate:  # find a same number as the one stored in the buffer
                count += 1
            else:
                count -= 1  # if new number come decrease coz chances are the candidate will not be more than a half
        return candidate


if __name__ == '__main__':
    theMajority = Solution()
    print(theMajority.findMajority([1, 2, 1, 1, 3, 4, 0]))  # should be None coz no majority
    print(theMajority.findMajority([2, 2, 1, 1, 1, 2, 2]))  # should be 2
    print(theMajority.findMajority([1, 2, 1, 1, 1, 2, 2]))  # should be 1
