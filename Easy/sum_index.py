class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        leftsum=0
        s=sum(nums)
        for i in range(0,len(nums)):
            if(leftsum == s-nums[i]-leftsum):
                return i
            leftsum+=nums[i]
        return -1
        
        
        
        
        
        '''
        if len(nums)==1:
            return 0
        for i in range(0,len(nums)):
            if(sum(nums[0:i])==sum(nums[i+1:len(nums)])):
                return i
        return -1
        ''' 
    