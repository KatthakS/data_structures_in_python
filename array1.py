#Given a binary array, find the maximum number of consecutive 1s in this array.

from typing import List

class maxOnesArray:
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        max_length = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                max_length = counter
                counter = 0
        return counter if counter>max_length else max_length

    nums = [1, 1, 0, 1, 1, 1]
    max_len = findMaxConsecutiveOnes(nums)
    print(max_len)