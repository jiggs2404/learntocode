class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        curmax=nums[0]
        globalmax=nums[0]
        for i in range(1,len(nums)):
            curmax=max(nums[i],nums[i]+curmax)
            if(globalmax<curmax):
                globalmax=curmax
        return globalmax