class Solution:
    def reverseVowels(self, s: str) -> str:
        st = list(s)
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        i , j = 0 , len(s)-1
        while i<j:
            if st[i] in vowels and st[j] in vowels:
                st[i] , st[j] = st[j] , st[i]
                i += 1 
                j -= 1
            elif st[i] in vowels:
                j -= 1
            elif st[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(st)

                        
        
            