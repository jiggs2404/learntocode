class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required={}
        for i in range(0,len(nums)):
            if(target-nums[i] in required):
                return([required[target-nums[i]],i])
            else:
                required[nums[i]]=i
        return [-1,-1]
        '''
        Array 
        [1,2,3,1,2,3,3,4]

        map={
        1:2
        2:2
        3:3
        }
        map = {}
        for(i in range):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] += 1

        max=0
        maxNum=0
        for i in range(maplength):
            if (max < map[nums[i]])
                max = map[nums[i]]      
                maxNum = nums[i]
        '''