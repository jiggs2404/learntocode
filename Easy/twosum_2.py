class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)
        while(i!=j):
            if(numbers[i]+numbers[j-1]==target):
                return[i+1,j]
            elif(numbers[i]+numbers[j-1]>target):
                j-=1
            elif(numbers[i]+numbers[j-1]<target):
                i+=1
        '''
        required={}
        for i in range(0,len(numbers)):
            if(target-numbers[i] in required):
                return([required[target-numbers[i]]+1,i+1])
            else:
                required[numbers[i]]=i
        return [-1,-1]
        '''
        