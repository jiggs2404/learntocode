class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        res=[]
        arr=[]
        if(m*n!=r*c):
            return mat
        for i in range(m):
            for j in range(n):
                arr.append(mat[i][j])
        ctr=0
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(arr[ctr])
                ctr+=1
            res.append(row)
        return res