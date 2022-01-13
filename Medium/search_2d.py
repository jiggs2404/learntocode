class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=(n*m)-1
        r=0
        c=0
        while(left<=right):
            mid=left+(right-left)//2  #mid=5
            r=mid//n  # 11 5//3=1
            c=mid%n   # 11 5%3=2
            if(matrix[r][c]==target):
                return True
            elif(matrix[r][c]<target):
                left=mid+1
            else:
                right=mid-1
        return False
            