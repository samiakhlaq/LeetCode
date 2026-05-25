class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        recheck = set()
        ans = [0, 0]
        act_sum = 0

        n = len(grid)

        for row in grid:
            for value in row:
                act_sum += value

                if value in recheck:
                    ans[0] = value

                recheck.add(value)

        exp_sum = n * n * (n * n + 1) // 2

        ans[1] = exp_sum + ans[0] - act_sum

        return ans


# ---------- Input Handling ----------
# In case you want to test in code editor.
# For submitting on LeetCode, you have to write just the first part of the code.

# if __name__ == "__main__":
#     n = int(input())  # size of grid (n x n)
#     grid = []

#     for _ in range(n):
#         row = list(map(int, input().split()))
#         grid.append(row)

#     obj = Solution()
#     print(obj.findMissingAndRepeatedValues(grid))

# In this code we use the concept of sum of first n natural numbers to find the missing and repeated values in the grid. We calculate the actual sum of the values in the grid and compare it with the expected sum to find the missing value. The repeated value is found by checking for duplicates while iterating through the grid.