'''
动态规划算法
要注意矩阵维度<2的边界情况。
'''
class Solution:
    _testing = True
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix)<1 or len(matrix[0])<1:
            return 0
        
        dp2=[[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        mx = 0
        for i in range(1,len(dp2)):
            for j in range(1, len(dp2[0])):
                if dp2[i][j]==1:
                    dp2[i][j] = min(dp2[i-1][j-1],dp2[i-1][j],dp2[i][j-1]) + 1
                    mx = max(mx, dp2[i][j])
        
        if mx==0:
            for i in range(len(dp2)):
                if dp2[i][0]==1:
                    return 1
            for j in range(len(dp2[0])):
                if dp2[0][j]==1:
                    return 1
        
        if Solution._testing: ###################
            print(dp2)
        return mx*mx