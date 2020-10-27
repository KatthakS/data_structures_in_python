"""
 Given an array nums,
 write a function to move all 0's to the end of it while maintaining the 
 relative order of the non-zero elements.
"""

from typing import List

class MoveAllZerosToRight:
    def move_zeros(nums: List[int]) -> None:
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        j = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[j] = nums[i]
                j += 1
        
        while j < len(nums):
            nums[j] = 0
            j += 1

    nums = [1, 0, 3, 2, 0]
    move_zeros(nums)
    print (nums)