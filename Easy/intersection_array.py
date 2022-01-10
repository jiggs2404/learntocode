class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        res=[]
        for i in range(0,1001):
            arr.append(0)
        for i in nums1:
            arr[i]+=1
        for i in nums2:
            if(arr[i]>0):
                arr[i]-=1
                res.append(i)        
        return res
        '''
        nums1.sort()
        nums2.sort()
        lst=[]
        i=0
        j=0
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]==nums2[j]):
                lst.append(nums1[i])
                i+=1
                j+=1
            elif(nums1[i]>nums2[j]):
                j+=1
            else:
                i+=1
        return lst
    
    
    i
    [4 ,9 ,5]
    j
    [9 ,4 ,9 ,8 ,4]
    
    sorted
    i
    [4 ,5 ,9]
    j
    [4 ,4 ,8 ,9 ,9]
    '''