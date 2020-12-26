"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
"""
#LeetCode top 100 liked questions - Medium
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for i in range(numRows)]
        delta = -1
        row = 0
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        for char in s:
            res[row].append(char)
            if row == 0 or row == numRows - 1:
                delta *= -1
            row += delta
        print (res)
        
        for i in range(len(res)):
            res[i] = ''. join(res[i])
        return ''.join(res)
        
ob = Solution()
print(ob.convert("SoftwareDevelopmentRocks", 3))