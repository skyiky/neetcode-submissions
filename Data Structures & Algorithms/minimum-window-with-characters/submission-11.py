from collections import Counter

class Solution:
    # dynamic sliding window approach, expand until valid, shrink until invalid
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        if len(t) > len(s):
            return result
        
        need = Counter(t)
        missing = len(t)

        l = 0 
        for r in range(len(s)):
            if s[r] in need:
                if need[s[r]] > 0:
                    missing -= 1
                need[s[r]] -= 1

            while missing == 0:
                if not result or r - l + 1 < len(result):
                    result = s[l:r+1]
                if s[l] in need:
                    need[s[l]] += 1
                    if need[s[l]] > 0:
                        missing += 1
                    
                l += 1

        return result
