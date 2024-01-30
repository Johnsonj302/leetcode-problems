class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        n = len(s)
        while s[n-1] == " ":
            n -= 1
        for i in range(n-1,-1,-1):
            if s[i] != " ":
                length += 1
            else:
                return length
        return length
