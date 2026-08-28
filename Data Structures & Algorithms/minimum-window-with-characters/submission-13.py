from collections import Counter

class Solution:
    # dynamic sliding window approach, expand until valid, shrink until invalid
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        result = ""
        need = Counter(t)
        have = 0

        l = 0 
        for r in range(len(s)):
            if s[r] in need:
                need[s[r]] -= 1
                have += 1 if need[s[r]] >= 0 else 0
            
            while have == len(t):
                if not result or r - l + 1 < len(result):
                    result = s[l:r+1]
                if s[l] in need:
                    need[s[l]] += 1
                    have -= 1 if need[s[l]] > 0 else 0                    
                l += 1

        return result
