class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        ans = 0
        for i in range(len(s)): # dynamic sliding window tracking a "seen" set, expand while valid, shrink when invalid and until valid again
            if s[i] not in seen:
                seen.add(s[i])
                ans = max(ans, i - start + 1)
            else:
                while s[i] in seen: # E.g. if s[i] == "A", remove characters until we can add back "A"
                    seen.remove(s[start])
                    start += 1
                seen.add(s[i])
        return ans