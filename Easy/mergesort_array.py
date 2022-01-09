class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=m-1
        p2=n-1
        i=m+n-1
        
        while(p2>=0):
            if(nums1[p1]>nums2[p2] and p1>=0):
                nums1[i]=nums1[p1]
                p1-=1
                i-=1
            else:
                nums1[i]=nums2[p2]
                p2-=1
                i-=1
        '''
        p1=m-1
        p2=n-1
        i=m+n-1
               p1        i
        [4 ,5 ,6 ,0 ,0 ,0]
               p2
        [1 ,2 ,3]
        
        
        for i in range(0,n):
            nums1[i+m]=nums2[i]
        nums1.sort()
        '''
        