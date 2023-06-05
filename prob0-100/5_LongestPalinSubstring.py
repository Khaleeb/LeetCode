class Solution:
    # First Solution
    def longestPalindrome(self, s: str) -> str:
        ml = 0
        mr = 0
        for i in range(len(s)):
            # check 2 focal
            if i+1 < len(s) and s[i] == s[i+1]:
                pal = 1
                r = i+1
                l = i
                while pal:
                    if r - l > mr - ml:
                        mr = r
                        ml = l
                    if (l-1 >= 0 and r+1 < len(s)) and s[l-1] == s[r+1]:
                        l-=1
                        r+=1
                    else:
                        pal = 0
            #check 1 focal
            pal = 1
            l = i
            r = i
            while(pal):                    # Combine these while loops for 1+2 focals into one loop that checks both for increased performance?
                if r - l > mr - ml:
                        mr = r
                        ml = l
                if (l-1 >= 0 and r+1 < len(s)) and s[l-1] == s[r+1]:
                    r+=1
                    l-=1
                else:
                    pal = 0
        return s[ml:(mr+1)]
    
#