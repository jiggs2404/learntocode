class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for i in range(0,len(magazine)):
            if magazine[i] not in dict:
                dict[magazine[i]] = 1
            else:
                dict[magazine[i]] +=1
        for i in range(0,len(ransomNote)):
            if ransomNote[i] in dict:
                if dict[ransomNote[i]] == 0:
                    return False
                else:
                    dict[ransomNote[i]]-=1
            else:
                return False
        return True