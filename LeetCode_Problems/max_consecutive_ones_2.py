"""
Given a binary array, 
find the maximum number of consecutive 1s 
in this array if you can flip at most one 0.
"""
#LeetCode Question 487 - Medium

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        front, end = 0, 0
        no_of_zero = 0
        largest_seq = 0
        while end < len(nums):
            if nums[end] == 0:
                no_of_zero += 1
                while no_of_zero == 2:
                    if nums[front] == 0:
                        no_of_zero -= 1
                    front = front+1
            largest_seq = max(largest_seq, end-front+1)
            end += 1
        return largest_seq

ob = Solution()
print(ob.findMaxConsecutiveOnes([1, 0, 1, 1, 0]))