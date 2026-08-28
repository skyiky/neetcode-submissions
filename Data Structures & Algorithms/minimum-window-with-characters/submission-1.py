class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        need = {}
        w = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        have = 0
        req = len(need)
        result = [-1, -1]
        result_len = float('inf')

        l = 0
        for r in range(len(s)): # invalid --> expand
            c = s[r]
            w[c] = w.get(c, 0) + 1

            if c in need and w[c] == need[c]:
                have += 1

            while have == req: # valid --> shrink
                if r - l + 1 < result_len:
                    result = [l, r]
                    result_len = r - l + 1
                
                lchar = s[l]
                w[lchar] -= 1

                if lchar in need and w[lchar] + 1 == need[lchar]:
                    have -= 1
                
                l += 1
        
        if result_len == float('inf'):
            return ""
        
        l, r = result
        return s[l:r+1]