class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a_pointer=0
        b_pointer=0
        if len(s1)>len(s2): return False
        s1_lst=[0]*26
        s2_lst=[0]*26
        #For first window
        for i in range(0,len(s1)):
            s1_lst[ord(s1[i])-ord('a')]+=1
            s2_lst[ord(s2[i])-ord('a')]+=1
        
        start=0
        for i in range(len(s1),len(s2)):
            if (s1_lst==s2_lst):
                return True
            s2_lst[ord(s2[i])-ord('a')]+=1
            s2_lst[ord(s2[start])-ord('a')]-=1
            start+=1
            
        if (s1_lst==s2_lst):
            return True
        return False
        
        