class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        unique = set()
        for i in range(len(s)):
            if s[i] in dict:
                if dict[s[i]] != t[i]:
                    return False
            else:
                if t[i] in unique:
                    return False

                dict[s[i]] = t[i]
                unique.add(t[i])
        return True