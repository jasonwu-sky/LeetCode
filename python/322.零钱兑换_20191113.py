'''
动态规划算法。子状态是amount更少的情况。具有最优子结构。
注意转移条件。
'''
class Solution:
    testing = False
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        coins.sort()    #coins并不是有序的。可以先排序，也可以全部遍历一遍
        for i in range(len(dp)):
            for j in range(len(coins)):
                if i-coins[j]<0 :    #coins并不是有序的。可以先排序，也可以全部遍历一遍
                    break
                if dp[i-coins[j]] > -1:    #这里一开始出错了，忘记判断是否存在dp[i-coins[j]]
                    if dp[i]<0:
                        dp[i] = dp[i-coins[j]]+1
                    else:
                        dp[i] = min(dp[i],dp[i-coins[j]]+1)
            if Solution.testing:    #############################
                print(i,dp)
        return dp[amount]