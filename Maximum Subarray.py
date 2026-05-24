class Solution(object):
    def maxSubArray(self, nums):
        current_Sum = 0
        max_Sum = nums[0]

        for i in nums:
            current_Sum += i
            max_Sum = max(max_Sum, current_Sum)
            if current_Sum < 0:
                current_Sum = 0

        return max_Sum


# ---------- Input Handling ----------
# In case you want to test in code editor. For submitting on Leetcode , you have to write just first part of the code 

#if __name__ == "__main__":
#    nums = list(map(int, input().split())) 
#    obj = Solution()
#    print(obj.maxSubArray(nums))

# In this code we use Kadane's Algorithm 
# Limitation of this algorithm: It will be failed when all of the elements of the array will be negative number . In that case this code will print 0 which will be wrong.
# For avoiding this limitation you can add(Instead of return max_Sum):

#      if current_Sum == 0 and Neg_Check(nums) == True:
#         return min(nums)
#      return max_Sum
#   def Neg_Check(nums):
#       for i in nums:
#            if i<0:
#               return True
#       return False