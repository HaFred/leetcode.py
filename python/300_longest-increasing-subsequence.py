"""Dynamic programming (DP), is good for problems that have multiple sub problems.

The core value is to come up with a dp table that records multiple states. That's how it's different from greedy algorithm. Because greedy algorithm only has the optimal solution directly without states changing.

5 steps of DP:
    1. Define dp array and its content
    2. Define state transferring function
    3. Initialize dp array
    4. Determine the sequence of state transferring
    5. Sub in example to verify the dp array holding correct elements

For instance, when dealing with the Fibonacci problem. With Step 5 using dp[10] as an example, we find that dp[0:10] == [0 1 1 2 3 5 8 13 21 34 55]. And for our code it needs to be matched.
"""


class Solution:
    def fib_solution_bigo_n(self, data_list, n):
        """tc: o(n), sc: o(n)"""
        if n == 0:  # get avoid with corner case
            return 0
        dp_arr = [0] * n
        dp_arr[0], dp_arr[1] = 0, 1
        output_model_list = []
        for i in data_list:
            dp_arr[i] = dp_arr[i - 1] + dp_arr[i - 2]
            output_model_list.append(dp_arr[i])
        print(output_model_list)

    def fib_solution_bigo_1(self, data_list):
        """tc: o(n), sc: o(1), coz neglecting input and output, here dp_arr is only with two elements"""
        dp_arr = [0] * 2
        dp_arr[0], dp_arr[1] = 0, 1
        output_model_list = []
        for i in data_list:
            temp = dp_arr[0]
            dp_arr[0] = dp_arr[1]
            dp_arr[1] = dp_arr[0] + temp
            output_model_list.append(dp_arr[1])
        print(output_model_list)

    def findLengthOfLCIS(self, nums) -> int:
        """ For longest continuous increasing subsequence: Leetcode Q674
        dp_arr ele is the length of the longest inc subseq of the current idx ele in input, which is ended with this current ele (important, otherwise cannot do comparison with the prev ele to update dp_arr intuitively).

        BigO: TC: O(n); SC: O(n).

        If using greedy algo. with two int vars count and result only, then TC==O(n), SC==O(1).
        """
        # dp arr init
        dp_arr = [1] * len(nums)
        result = 1
        for i in range(len(nums) - 1):  # no need to do one more layer of for loop since it's LCIS rather than LIS
            if nums[i + 1] > nums[i]:
                dp_arr[i + 1] = dp_arr[i] + 1
                result = max(result, dp_arr[i + 1])  # with a minimum 1, to avoid some negative number as the input to mess up
        return result

    def findLengthOfLIS(self, nums) -> int:
        """For longest increasing subsequence: Leetcode Q300

        BigO: TC: O(n^2); SC: O(n)
        """
        dp_arr = [1] * len(nums)  # dp arr init, the length of current idx's LIS
        result = 1
        for i in range(len(nums)):  # start handling from the nums[1]
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_arr[i] = max(dp_arr[i], dp_arr[j] + 1)
                    result = max(result, dp_arr[i])
        return result


if __name__ == '__main__':
    s = Solution()

    # # for fib seq testing, a simple example for the dp problems
    # input_list = [2, 3, 4]
    # output_gt_list = [1, 2, 3]
    # # s.fib_solution_bigo_n(input_list, 10)
    # s.fib_solution_bigo_1(input_list)

    # # for lcis
    # # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # # output_gt = 4
    # nums = [1, 3, 5, 4, 7]
    # # nums = [1,3,5,4,7]
    # # nums = [2,1]
    # # output_gt = 3
    # out = s.findLengthOfLCIS(nums)
    # print(out)

    # for lis problem, if brute-force tc will be o(n^2)
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [0, 1, 0, 3, 2, 3]
    out = s.findLengthOfLIS(nums)
    print(out)

