class Solution(object):
    def maxProfit(self, prices):
        min_buy = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_buy:
                min_buy = price
            else:
                max_profit = max(max_profit, price - min_buy)

        return max_profit


# ---------- Input Handling ----------
# if __name__ == "__main__":
#     prices = list(map(int, input().split()))
#     obj = Solution()
#     print(obj.maxProfit(prices))

# In this code we keep track of the minimum price we have seen so far and the maximum profit we can achieve. We iterate through the list of prices, updating the minimum price and calculating the potential profit at each step. Finally, we return the maximum profit found.