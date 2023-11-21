"""Given two string arrays words1 and words2, return the number
 of strings that appear exactly once in each of the two arrays."""

def countWords(words1,words2):
    count=0
    for word in words1:
        if words1.count(word)==1 and words2.count(word) ==1:
            
            count +=1
    return count

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]

print(countWords(words1,words2))
