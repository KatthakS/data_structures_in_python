#Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
"""
Contraints: 
    - 1 <= arr.length <= 10000
    - 0 <= arr[i] <= 9
"""
from typing import List
class DuplicateZeros:
    def duplicateZerosInTheList(arr: List[int]) -> None:
        i = 0
        while (i < len(arr)):
            if arr[i] == 0:
                for j in range(len(arr)-1, i, -1):
                    arr[j] = arr[j-1]
                arr[j] = 0
                i+=2
            else:
                i+=1
    arr = [1, 0, 0, 1, 1]
    print ("Before", arr)
    duplicateZerosInTheList(arr)
    print ("After", arr)