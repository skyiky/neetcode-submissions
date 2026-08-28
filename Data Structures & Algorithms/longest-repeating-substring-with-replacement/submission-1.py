from collections import defaultdict
class Solution:
    # sliding window
    # mininum replacements needed = window size - frequency of most common character
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = defaultdict(int)
        l = 0
        for r, rc in enumerate(s):
            count[rc] += 1
        
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest
        