# give an array nums consisting of 2n elements in the form [x1,x2,x3.....xn,y1,y2,y3....yn].
# Return the array in the form [x1,y1,x2,y2...xn,yn].
class Solution:
    def shuffle(self, nums, n):
        new_list = []
        for i in range(len(nums)//2):
            new_list.append(nums[i])
            new_list.append(nums[i+n])
        return new_list
    
nums = [2,5,1,3,4,7]
n = 3
s = Solution()
ans= s.shuffle(nums,n)
print(ans)