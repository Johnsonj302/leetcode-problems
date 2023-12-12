"""Count Integers With Even Digit Sum
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits
"""
class Solution:
    def countEven(self, num: int) -> int:
        return sum(1 for i in range(1, num + 1) if sum(int(digit) for digit in str(i)) % 2 == 0)

       #-----------OR-----------

class Solution:
    def countEven(self, num: int) -> int:    
        count =0
        for i in range(1,num+1):
            digit  = str(i)
            dsum =0
            for j in range(len(digit)):
                dsum += int(digit[j])
            if dsum %2 == 0:
                count +=1
        return count
       