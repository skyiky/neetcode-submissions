from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = [-1, -1]
        result_len = float('inf')

        if len(t) > len(s):
            return ""
        
        target = Counter(t)
        curr = Counter()
        req = len(target)
        met = 0

        l = 0 
        for r in range(len(s)): # expand until valid
            curr.update(s[r])
            if s[r] in target and curr[s[r]] == target[s[r]]:
                met += 1
            while met == req: # shrink until invalid
                if r - l + 1 < result_len: # track result
                    result_len = r - l + 1
                    result = [l, r]
                curr.subtract(s[l])
                if s[l] in target and curr[s[l]] < target[s[l]]:
                    met -= 1
                l += 1

        if result_len == float('inf'):
            return ""
        else:
            l, r = result
            return s[l:r+1]
            
        
                
                


            

        
        