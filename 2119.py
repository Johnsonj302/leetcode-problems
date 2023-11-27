"""Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 
          321 as the leading zeros are not retained.

Given an integer num, reverse num to get reversed1, then reverse reversed1 to 
get reversed2. Return true if reversed2 equals num. Otherwise return false."""

def A_Number_After_a_Double_Reversal(num):
    
    return False if num%10 == 0 and num != 0 else True

#num = 526    ans---->True
#num = 1800   ans---->False
num = 0     # ans---->True

print(A_Number_After_a_Double_Reversal(num))
