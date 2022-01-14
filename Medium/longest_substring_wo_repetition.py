class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a_pointer=0
        b_pointer=0
        max_len=0
        lst=[]
        while(b_pointer<len(s)):
            if(s[b_pointer] not in lst):
                lst.append(s[b_pointer])
                b_pointer+=1
                max_len=max(max_len,len(lst))
            else:
                lst.remove(s[a_pointer])
                a_pointer+=1
        return max_len
        # sliding window problem
                
                    