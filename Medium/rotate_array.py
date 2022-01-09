class Solution:
    def revarray(self,num: List[int], start,end: int) -> None:
        while(start<end):
            temp=num[start]
            num[start]=num[end]
            num[end]=temp
            start+=1
            end-=1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        self.revarray(nums,0,len(nums)-1)
        self.revarray(nums,0,k-1)
        self.revarray(nums,k,len(nums)-1)
        
        '''
        [1 ,2 ,3 ,4 ,5 ,6 ,7]
            
        Step1: Reverse poora array
        [7, 6, 5, 4, 3, 2, 1]
        Step2: Reverse from 0 to k-1
        [7, 6, 5, 4, 3, 2, 1]
        
        Step 3: Reverse from k to end
        [1, 2, 3, 4, 5, 6, 7]
        '''