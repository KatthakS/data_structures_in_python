#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#Leetcode top 100 Liked Questions

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}
        for i in range(len(nums)):
            if target - nums[i] in rem:
                return rem[target-nums[i]],i
            else:
                rem[nums[i]] = i

input_list = [2,8,12,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))