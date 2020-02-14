'''
动态规划算法。
python初始化二维数组的方法。  [[0 for j in range(n)] for i in range(m)]
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m<1 or n<1:
            return 0
        dp2 = [[0 for j in range(n)] for i in range(m)]  #初始化二维数组
        for i in range(m):
            dp2[i][0] = 1
        for j in range(1,n):
            dp2[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp2[i][j] = dp2[i-1][j] + dp2[i][j-1]
        
        
        return dp2[m-1][n-1]