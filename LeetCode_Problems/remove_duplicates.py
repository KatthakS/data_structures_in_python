#Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

from typing import List
class RemoveDuplicateValuesFromArray:
    def removeDuplicates(nums: List[int]) -> int:
        i = 0
        j = 0
        for j in range(j+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            else:
                i += 1
                nums[i] = nums[j]
        return i+1
                
    nums = [1, 1, 2, 2, 2, 2, 3, 3]
    recv_val = removeDuplicates(nums)
    for i in range(0, recv_val):
        print (nums[i])