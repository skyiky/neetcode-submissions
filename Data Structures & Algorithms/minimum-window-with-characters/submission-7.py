from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = [-1, -1]
        result_len = float('inf')
        
        if not t or len(s) < len(t):
            return ""

        target = Counter(t)
        curr = Counter()
        met = 0

        l = 0
        for r in range(len(s)): # invalid --> expand
            curr.update(s[r]) # update window data

            if s[r] in target and curr[s[r]] == target[s[r]]: # check match?
                met += 1

            while met == len(target): # valid --> shrink
                if r - l + 1 < result_len: # window smaller?
                    result = [l, r]
                    result_len = r - l + 1
                
                curr.subtract(s[l])

                if s[l] in target and curr[s[l]] < target[s[l]]: # check not match?
                    met -= 1
                
                l += 1
        
        if result_len == float('inf'):
            return ""
        
        l, r = result
        return s[l:r+1]