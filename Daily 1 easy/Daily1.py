#Good morning! Here's your coding interview problem for today.
#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

import os

arr = [10, 15, 4, 3]
k = 14

def numsEquals(nums, target):

    for x in range(len(nums)):

        remainder = target - nums[x]

        if remainder in nums:
            return True
        
    return False



print(numsEquals(arr,k))
    
