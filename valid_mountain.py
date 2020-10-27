"""
Given an array nums of integers, return true if and only if it is a valid mountain array.

Recall that nums is a mountain array if and only if:
    - nums.length >= 3
    - There exists some i with 0 < i < nums.length - 1 such that:
        * nums[0] < nums[1] < ... nums[i-1] < nums[i]
        * nums[i] > nums[i+1] > ... > nums[nums.length - 1]
"""

from typing import List
class IsValidMountain:
    def valid_mountain_array(nums: List[int]) -> bool:
        i = 1
        if len(nums) < 3:
            return 0
        
        while (i < len(nums)):
            if(nums[i-1] < nums[i]):
                i += 1
            else:
                break
        if (i == len(nums) or i == 1):
            return 0
        else:
            while (i < len(nums)):
                if(nums[i-1] > nums[i]):
                    i += 1
                else:
                    return 0
        return 1

    nums = [1, 4, 3, 2, 1]
    val = valid_mountain_array(nums)
    if(val):
        print('valid mountain')
    else:
        print('invalid mountain')