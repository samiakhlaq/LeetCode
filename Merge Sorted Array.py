class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k = m + n - 1  # Updated nums1 index
        m -= 1
        n -= 1

        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1
            k -= 1

        return nums1


# ---------- Input Handling ----------
# if __name__ == "__main__":
#     m = int(input())
#     nums1 = list(map(int, input().split()))
#     n = int(input())
#     nums2 = list(map(int, input().split()))
#
#     obj = Solution()
#     obj.merge(nums1, m, nums2, n)
#     print(nums1)

# In this code we use three pointers to merge the two sorted arrays. We start from the end of both arrays and compare the elements. We place the larger element at the end of nums1 and move the pointers accordingly until we have merged all elements from nums2 into nums1.