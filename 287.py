class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique_number = set()
        for num in nums:
           if num in unique_number:
            return num
           unique_number.add(num)
        