#Given an array nums of integers, return how many of them contain an even number of digits.
#Constraints:
    #1 <= nums.length <= 500
    #1 <= nums[i] <= 10^5

from typing import List

class EvenNumberofDigits:
    def findNumbers(nums: List[int]) -> int:
        count = 0
        for i in nums:
            if(i % 100000) < i:
                count += 1
            else:
                # Definitely we dont have a 6 digit number
                if (i % 10000) < i:
                    #5 digit no.
                    print (i, "is 5 digit number")
                else:
                    if (i % 1000) < i:
                        #4 digit no.
                        count += 1
                    else:
                        if (i % 100) < i:
                            #3 digit no.
                            print (i, "is 3 digit number")
                        else:
                            if (i % 10) < i:
                                #2 digit no.
                                count +=1
                            else:
                                #1 digit no.
                                print (i, "is 1 digit number")

        return count

    nums = [10, 11111, 1]
    max = findNumbers(nums)
    print ("Total integers having even number of digits: ", max)
    