'''
在左侧与右侧各选出一个最高值。min(L,R)即为该位置能接的雨水
也可以用双指针法
'''
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if len(height)<3 :
#             return 0
#         L = [0 for i in range(len(height))]
#         R = L[:]
#         for i in range(1,len(height)):    #左侧的最高值
#             L[i] = max(L[i-1],height[i-1])
#         for i in range(len(height)-2,-1,-1):    #右侧的最高值
#             R[i] = max(R[i+1],height[i+1])
#         res = 0
#         for i in range(1,len(height)-1):
#             res = res + max(0, min(L[i],R[i])-height[i])
#         return res


'''
双指针法
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        L_max = R_max = 0
        L =0
        R = len(height)-1
        while L<R:
            if height[L]<=height[R]:    #左侧更新
                if height[L] > L_max:
                    L_max = height[L]
                else:
                    res += L_max-height[L]
                L+=1
            else:    #右侧更新
                if height[R] > R_max:
                    R_max = height[R]
                else:
                    res += R_max-height[R]
                R-=1
        
        return res