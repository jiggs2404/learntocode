class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        arr=[1]
        res.append(arr)
        if(numRows==1):
            return res
        for i in range(1,numRows):
            curRow=[1]
            prevRow=[]
            prevRow=res[i-1]
            for j in range(1,i):
                curRow.append(prevRow[j-1]+prevRow[j])
            curRow.append(1)
            res.append(curRow)
        return res
            
            
        '''
        [
        [1]
        [1,1]
        [1,2,1]
        [1,3,3,1]
        ]
        
        '''