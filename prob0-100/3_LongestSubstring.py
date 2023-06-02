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