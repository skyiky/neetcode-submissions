class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def dupe(strs: List[str]) -> bool:
            hmap = {}
            for s in strs:
                if s != ".":
                    if s in hmap:
                        return True
                    hmap[s] = 1
            return False
        
        for i in range(9):
            row = board[i]
            if dupe(row):
                return False
        
        for i in range(9):
            col = [row[i] for row in board]
            if dupe(col):
                return False
        
        for i in range(0, 9, 3):
            a, d, g, = board[i][0:3], board[i][3:6], board[i][6:9]
            b, e, h, = board[i+1][0:3], board[i+1][3:6], board[i+1][6:9]
            c, f, i, = board[i+2][0:3], board[i+2][3:6], board[i+2][6:9]
            if dupe(a+b+c) or dupe(d+e+f) or dupe(g+h+i):
                return False
        
        return True
        