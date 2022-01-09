class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=0
        for i in range(0,len(digits)):
            a=a*10+digits[i]
        a=a+1
        lst=[]
        x=0
        while(a>0):
            x=a%10
            lst.append(x)
            a=a//10
        lst.reverse()
        return lst