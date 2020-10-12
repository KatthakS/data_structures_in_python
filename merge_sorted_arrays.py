# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

"""
Constraints:
    * -10^9 <= nums1[i], nums2[i] <= 10^9
    * m = number of elements in nums1
    * n = number of elements in nums2
    * nums1.length == m + n
    * nums2.length == n
"""

from typing import List

class MergeSortedArrays:
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = len(nums1) - 1
        
        m-=1
        n-=1
        while (m >= 0) and (n >= 0):
            if nums1[m] >= nums2[n]:
                nums1[l1] = nums1[m]
                m -= 1
            else:
                nums1[l1] = nums2[n]
                n -= 1
            l1 -= 1
        
        while n >= 0:
            nums1[l1] = nums2[n]
            n-=1
            l1-=1

    nums1 = [2, 2, 3, 0, 0, 0]
    nums2 = [1, 5, 6]
    merge(nums1, 3, nums2, 3)   
    print (nums1)     