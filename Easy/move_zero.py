class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0 
        j=0
        while(i<len(nums)):
            if(nums[i]!=0):
                nums[j]=nums[i]
                i+=1
                j+=1
            else:
                i+=1
        while(j<len(nums)):
            nums[j]=0
            j+=1
        
        '''
        c=0
        for i in range(0,len(nums)):
            if nums[i]==0:
                c+=1
        if c>0:
            for i in range(0,c):
                nums.remove(0)
                nums.append(0)

        i
        [0 ,1 ,0 ,3 ,12]
        j
        '''