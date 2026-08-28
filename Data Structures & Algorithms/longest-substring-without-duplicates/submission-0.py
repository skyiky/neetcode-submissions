class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        ans = 0
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                ans = max(ans, i - start + 1)
            else:
                while s[i] in seen:
                    seen.remove(s[start])
                    start += 1
                seen.add(s[i])
        return ans