"""2148. Count Elements With Strictly Smaller and Greater Elements

Given an integer array nums, return the number of elements that have
 both a strictly smaller and a strictly greater element appear in nums."""

def countElements(nums):
        count = 0
        smallest_number = min(nums)
        largest_number = max(nums)
        for i in nums:
            if smallest_number < i < largest_number:
                count +=1
        return count

#nums = [11,7,2,15]
nums = [-3,3,3,90]

print(countElements(nums))
