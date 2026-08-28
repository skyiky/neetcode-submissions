class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = [-1, -1]
        result_len = float('inf')
        
        if not t or len(s) < len(t):
            return ""

        t_freq = {}
        w_freq = {}

        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        matches = 0
        required_matches = len(t_freq)

        l = 0
        for r in range(len(s)): # invalid --> expand
            c = s[r]
            w_freq[c] = w_freq.get(c, 0) + 1 # c --> update window data

            if c in t_freq and w_freq[c] == t_freq[c]: # c --> check match?
                matches += 1

            while matches == required_matches: # valid --> shrink
                if r - l + 1 < result_len: # window smaller?
                    result = [l, r]
                    result_len = r - l + 1
                
                c = s[l]
                w_freq[c] -= 1

                if c in t_freq and w_freq[c] + 1 == t_freq[c]:
                    matches -= 1
                
                l += 1
        
        if result_len == float('inf'):
            return ""
        
        l, r = result
        return s[l:r+1]