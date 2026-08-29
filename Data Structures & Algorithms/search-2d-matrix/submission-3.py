class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])
        
        # Find the right row
        l , r = 0, n * m - 1

        while(l <= r):
            mid = l + (r - l)//2
            row = mid // m
            col = mid % m

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1

        return False