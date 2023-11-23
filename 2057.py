"""Smallest Index With Equal Value"""

"""Given a 0-indexed integer array nums, return the smallest index i of nums 
such that i mod 10 == nums[i], or -1 if such index does not exist.

x mod y denotes the remainder when x is divided by y."""

def Smallest_Index_With_Equal_Value(nums):
    return next((i for i in range(len(nums)) if i%10 == nums[i]),-1)


nums = [1,2,3,4,5,6,7,8,9,0]
print(Smallest_Index_With_Equal_Value(nums))