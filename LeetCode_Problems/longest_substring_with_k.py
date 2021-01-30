"""
Given a string s and an integer k, 
return the length of the longest substring of s that contains at most k distinct characters.
Leetcode - Medium
"""

from collections import defaultdict
class Solution():
    def lengthOfLongestSubstringKDistinct(self, s:str, k:int)->int:
        """
            Input: s = "eceba", k = 2
            Output: 3
            Explanation: The substring is "ece" with length 3.
        """
        str_len = len(s)
        if str_len < k:
            return str_len
        elif k == 0:
            return k
        
        start, end = 0, 0
        max_len = 1
        d = defaultdict()
        while end < str_len:
            d[s[end]] = end
            end += 1
            if len(d) > k :
                dlt_idx = min(d.values())
                del d[s[dlt_idx]]
                start = dlt_idx + 1
            max_len = max(max_len, end-start)
        return max_len

ob = Solution()
print(ob.lengthOfLongestSubstringKDistinct("abcbbbbcccbdddadacb", 2))