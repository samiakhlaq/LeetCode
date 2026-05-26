class Solution(object):
    def myPow(self, x, n):

        ans = 1

        if n == 1: return x
        if n == 0: return 1
        if n == -1: return 1 / x

        if x == 1: return 1
        if x == 0: return 0
        if x == -1:
            if n % 2 == 0: return 1
            else: return -1

        if n < 0:
            n = -n
            x = 1 / x

        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2

        return ans


# ---------- Input Handling ----------
# if __name__ == "__main__":
#     x = float(input())
#     n = int(input())
#     obj = Solution()
#     print(obj.myPow(x, n))

# In this code we use binary exponentiation (fast power) to calculate x^n efficiently.
# Instead of multiplying x n times, we reduce the exponent by repeatedly squaring the base.
# If the current exponent bit is 1 (odd), we multiply the result with the current base.
# If n is negative, we convert the problem into positive exponent by taking reciprocal of x.
# This approach reduces time complexity from O(n) to O(log n), making it very efficient.