class Solution:
    # Divide tells you the row. Remainder tells you how far across.
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows*cols-1
        while l <= r:
            mid = (r - l) // 2 + l
            y = mid // cols
            x = mid % cols
            y, x = divmod(mid, cols)
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                l = mid+1
            else:
                r = mid-1
        return False
