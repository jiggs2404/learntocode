class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst=[None]*len(nums)
        low=0
        high=len(nums)-1
        index=len(nums)-1
        while(low<=high):
            if(abs(nums[high])>abs(nums[low])):
                lst[index]=nums[high]*nums[high]
                high=high-1
            else:
                lst[index]=nums[low]*nums[low]
                low=low+1
            index=index-1
        return lst