'''
贪心算法
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        mx = 0
        value = 0
        for i in range(1,len(prices)):
            value = max(0, prices[i]-prices[i-1]+value)
            mx = max(mx, value)
        return mx