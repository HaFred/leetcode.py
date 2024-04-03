class Solution:
    def count_of_distinct_graphs(self, N):
        return 2 ** (N * (N - 1) // 2)

    def test(self, n):
        MOD = int(1e9 + 7)

        # Function to return the count of distinct
        # graphs possible with n vertices
        def countGraphs(n):
            # Maximum number of edges for a
            # graph with n vertices
            x = (n * (n - 1)) // 2

            # Return 2 ^ x
            return (pow(2, x, MOD))

        # Driver code
        n = 5
        print(countGraphs(n))

Input = 3
Output = 8
s = Solution()
s.test(4)
# Input = 4
# Output = 64
