class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return(False)
        else:
            t=x
            new=0
            while(x!=0):
                n=x%10
                new=new*10+n
                x=x//10
            if(t==new):
                return(True)
            else:
                return(False)