import os

arr = [10, 15, 4, 7]
k = 18

def numsEquals(nums, target):

    for x in range(len(nums)):

        remainder = target - nums[x]

        if remainder in nums:
            return True
        
    return False



print(numsEquals(arr,k))
    