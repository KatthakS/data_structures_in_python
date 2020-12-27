"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
#Leetcode Array Question - Medium

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_list = []
        for interval in intervals:
            if len(merged_list) == 0 or merged_list[-1][1] < interval[0]:
                merged_list.append(interval)
            elif merged_list[-1][1] >= interval[0]:
                merged_list[-1][1] = max(merged_list[-1][1], interval[1])
        return merged_list

ob = Solution()
print(ob.merge([[1,3],[2,6],[8,10],[15,18]]))