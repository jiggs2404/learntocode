class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        maxnum=0
        a=-1
        for i in range(0,len(nums)):
            if(maxnum<nums[i]):
                maxnum=nums[i]
                a=i
        for i in range(0,len(nums)):
            if nums[i]*2>maxnum and nums[i]!=maxnum:
                return -1
        return a
    
   