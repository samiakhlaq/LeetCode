class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i

        # ---------- Input Handling ----------
        # if __name__ == "__main__":
        #     nums = list(map(int, input().split()))
        #     target = int(input())
        #     obj = Solution()
        #     print(obj.twoSum(nums, target))

        # ---------- Process Explanation ----------
        # This code uses a hash map (dictionary) to solve the Two Sum problem efficiently.
        # For each element, we calculate its complement (target - current value).
        # If the complement already exists in the map, we return the stored index and current index.
        # Otherwise, we store the current number with its index for future lookup.
        # This ensures a single-pass solution with time complexity O(n)
        # and space complexity O(n).