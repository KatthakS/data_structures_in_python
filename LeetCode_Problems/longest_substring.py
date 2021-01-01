#Given a string s, find the length of the longest substring without repeating characters.
#Leetcode top 100 Liked Questions

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_dict = {}
        longest = 0
        current_length = 0
        current_sub_start = 0
        
        for i, letter in enumerate(s):
            if letter in sub_dict and sub_dict[letter] >= current_sub_start:
                current_sub_start = sub_dict[letter]+1
                sub_dict[letter] = i
                current_length = i - current_sub_start + 1
            else:
                sub_dict[letter] = i
                current_length = i - current_sub_start + 1
                longest = max(longest, current_length)
        return longest 

ob = Solution()
print(ob.lengthOfLongestSubstring("abcabcbb"))