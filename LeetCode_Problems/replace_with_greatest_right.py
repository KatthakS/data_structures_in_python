#Given an array arr, replace every element in that array with the greatest element among the elements to its right, 
# and replace the last element with -1.

from typing import List
class ReplaceWithGreatestRight:
    def replace_elements(arr: List[int]):
        i = 1
        while i<=len(arr):
            if i == len(arr):
                arr[i-1] = -1
            else:
                arr[i-1] = max(arr[i:])
            i += 1
    arr = [17, 18, 5, 4, 6, 1]
    replace_elements(arr)
    print(arr)
        