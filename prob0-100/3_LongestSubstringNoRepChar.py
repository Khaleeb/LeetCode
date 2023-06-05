class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxtuple = (0, 0)
        if len(s) < 1:
            return 0
        if len(s) == 1:
            return 1
        for i in range(0,len(s)):
            usedList = []
            flag = 1
            d = 0
            while(flag):
                if(s[i+d] not in usedList):
                    usedList.append(s[i+d])
                    if (i+d+1 < len(s)):
                        d+=1
                    else: 
                        flag = 0
                        if maxtuple[1] < d:
                            maxtuple = (i, d)
                else:
                    flag = 0
                    if maxtuple[1] < d:
                        maxtuple = (i, d-1)
        # print(s[maxtuple[0]:maxtuple[1]])
        return maxtuple[1]+1
    



## Thank you, LeetCode, for this solution:
class BetterSolution:
    def lengthOfLongsetSubstring(self, s: str) -> int:
        def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        l = 0
        r = 0
        while(r < len(s)):
            if s[r] not in s[l:r]:
                r+=1
                if max < r-l:
                    max = r-l
            else:
                l+=1
        return max
