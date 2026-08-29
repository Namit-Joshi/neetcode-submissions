class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])
        
        # Find the right row
        l , r = 0, n - 1
        row = 0

        while(l <= r):
            mid = l + (r - l)//2
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                row = mid
                l = mid + 1
            else:
                r = mid - 1


        # Find inside row

        l, r = 0, m - 1

        while(l <= r):
            mid = l + (r - l)//2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1

        return False