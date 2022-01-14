class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        mdict = {}
        rdict={}
        for i in range(0,len(s)):
            if s[i] not in mdict:
                mdict[s[i]] = 1
            else:
                mdict[s[i]] +=1
            if t[i] not in rdict:
                rdict[t[i]] = 1
            else:
                rdict[t[i]] +=1
                
        if(rdict==mdict):
            return True
        else:
            return False