class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(strs == None or strs[0] == ""):
            return ""
        if(len(strs)==1):
            return strs[0]
        strs.sort()
        s=min(len(strs[0]),len(strs[len(strs)-1]))
        i=0
        while(i<s and strs[0][i]==strs[len(strs)-1][i]):
                i+=1
       
        return strs[0][0:i]