"""Given an array of strings words, return the first palindromic string 
    in the array. If there is no such string, return an empty string "".

    A string is palindromic if it reads the same forward and backward."""

def first_palindromic_string(words):
    return next((word for word in words if word == word[::-1]),"")


#words = ["abc","car","ada","racecar","cool"]  output ada
# words = ["notapalindrome","racecar"]         output racecar
words = ["def","ghi"] #                        outpot 
print(first_palindromic_string(words))