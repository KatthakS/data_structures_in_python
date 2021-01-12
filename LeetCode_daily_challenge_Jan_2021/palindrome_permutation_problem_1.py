"""
Problem No: 1
Given a string, determine if a permutation of the string could form a palindrome.
Example 1:

Input: "code"
Output: false

Example 2:

Input: "aab"
Output: true

Example 3:

Input: "aabc"
Output: false

"""
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        
        dict = {}
        count = 0
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict[s[i]] = 1
                
        for j in dict:
            if dict[j] % 2 != 0:
                count += 1
        if count <= 1:
            return True
        return False
            
ob = Solution()
print(ob.canPermutePalindrome("code"))