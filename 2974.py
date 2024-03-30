class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums)
        while n:
            if n:
                min1 = min(nums)
                nums.remove(min1)
                min2 = min(nums)
                arr.append(min2)
                arr.append(min1)
                nums.remove(min2)
                n = len(nums)
               
        return arr
            