class Solution(object):
    def singleNumber(self, nums):
        single = 0
        for each in nums:
            single ^= each
        return single


# ---------- Input Handling ----------
# if __name__ == "__main__":
#     nums = list(map(int, input().split()))
#     obj = Solution()
#     print(obj.singleNumber(nums))

# In this code we use the XOR operator to find the single number. The XOR of a number with itself is 0 and the XOR of a number with 0 is the number itself. Therefore, by XORing all the numbers in the array, we will be left with the single number that does not have a duplicate.