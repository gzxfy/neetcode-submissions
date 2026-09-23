class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        max_stock = 0

        for i in range(1, len(prices)):
            result = prices[i] - prices[left]

            if result > 0:
                max_stock = max(max_stock, result)
            else:
                left = i

        return max_stock