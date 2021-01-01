# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

from typing import List
class RemoveSpecificElements:
    def removeElement(nums: List[int], val: int) -> int:
        length = 0
        i = 0
        while i < len(nums):
            if i + length == len(nums):
                break
            if nums[i] == val:
                for j in range(i, len(nums)-1):
                    nums[j] = nums[j+1]
                nums[len(nums)-1] = val
                length += 1
            else:
                i+=1
        return len(nums) - length
    nums = [3, 2, 2, 3]
    recv_length = removeElement(nums, 3)
    for i in range(0, recv_length):
        print(nums[i])