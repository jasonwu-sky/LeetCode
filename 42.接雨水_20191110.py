'''
在左侧与右侧各选出一个最高值。min(L,R)即为该位置能接的雨水
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3 :
            return 0
        L = [0 for i in range(len(height))]
        R = L[:]
        for i in range(1,len(height)):    #左侧的最高值
            L[i] = max(L[i-1],height[i-1])
        for i in range(len(height)-2,-1,-1):    #右侧的最高值
            R[i] = max(R[i+1],height[i+1])
        res = 0
        for i in range(1,len(height)-1):
            res = res + max(0, min(L[i],R[i])-height[i])
        return res