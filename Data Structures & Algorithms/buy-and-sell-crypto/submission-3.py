class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        result = 0

        for right in range(1, len(prices)):
            difference = prices[right] - prices[left]
            
            if difference > 0:
                result = max(result, difference)
            else:
                left = right



        return result
        