"""
 Given an m x n binary matrix filled with 0's and 1's, 
 find the largest square containing only 1's and return its area.
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
Output: 4
"""
#LinkedIn top 100 liked questions - medium

from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        max_len = 0
        dp = [[0 for i in range(c)]for j in range(r)]
        
        for i in range(r):
            if int(matrix[i][0]) == 1:
                max_len = 1
            dp[i][0] = int(matrix[i][0])
            
        for j in range(c):
            if int(matrix[0][j]) == 1:
                max_len = 1
            dp[0][j] = int(matrix[0][j])

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                if dp[i][j] > max_len:
                    max_len = int(dp[i][j])


        return max_len**2

ob = Solution()
print(ob.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))