'''
回溯法
这个题，要注意
'''

class Solution:
    testing = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(board, word, flag, i=0, j=0, k=0):
            if Solution.testing:   #################################
                print(board,' i:',i,' j:',j,' k:',k)
            if flag[0] == True:
                return
            letter = word[k]
            if letter != board[i][j]:
                return
            else:
                if k+1==len(word):
                    flag[0] = True
                    return
                
                board[i][j] = '#'
                if j<len(board[0])-1:
                    backtrack(board, word, flag, i, j+1, k+1)
                if i<len(board)-1:
                    backtrack(board, word, flag, i+1, j, k+1)
                if j>0:
                    backtrack(board, word, flag, i, j-1, k+1)
                if i>0:
                    backtrack(board, word, flag, i-1, j, k+1)
                board[i][j] = letter
            return
        
        flag = [False]
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(board, word, flag,i,j,0)
                if flag[0]==True:
                    return True
        return flag[0]
