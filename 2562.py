class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
       index =-1 
       result = []
       for i in range(len(nums)//2):
           result.append(int(str(nums[i]) + str(nums[index])))
           index -=1

       if len(nums)%2 == 0:
           return sum(result)
       else:
           return sum(result) + nums[len(nums)//2]

