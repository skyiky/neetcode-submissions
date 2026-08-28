class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = [n for row in matrix for n in row]
        l, r = 0, len(x)-1
        while l <= r:
            mid = (r - l // 2) + l
            if x[mid] == target:
                return True
            elif x[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return False