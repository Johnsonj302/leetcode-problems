class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0] + nums[1]
        n = len(nums)
        count = 1
        for i in range(2,n,2):
            if i+1 < n:
                s = nums[i] + nums[i+1]
                if score == s:
                    count += 1
                else:
                    break

        return count        





        