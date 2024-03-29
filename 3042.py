class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1,str2):
            n1 = len(str1)
            n2 = len(str2)
            if n1 <= n2:
                if str1 == str2[:n1] and str1 == str2[n2-n1:]:
                    return 1
            else:
                return 0
            
        num = 0
        for  i in range(len(words)-1):
            for j in range(i+1,len(words)):
                count = isPrefixAndSuffix(words[i],words[j])
                if count:
                    num += 1
        return num