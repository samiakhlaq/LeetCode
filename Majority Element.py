class Solution(object):
    def majorityElement(self, nums):
        freq = 0
        ans = 0

        for value in nums:
            if freq == 0:
                ans = value
            if ans == value:
                freq += 1
            else:
                freq -= 1

        if freq > 0:
            return ans
        return 0  # This will not affect this particular problem as the problem ensures that there will be a majority element.


# ---------- Input Handling ----------
# In case you want to test in code editor.
# For submitting on LeetCode, you have to write just the first part of the code.

# if __name__ == "__main__":
#     nums = list(map(int, input().split()))
#     obj = Solution()
#     print(obj.majorityElement(nums))

# In this code we use Boyer-Moore Voting Algorithm which is based on the principle of canceling out each occurrence of an element e with all the other elements that are different from e.
