from collections import Counter 
class Solution:
    # fixed size window, compare s1 with s2 at every possible position 
    # X l e c a b e e
    # X a b c
    # X   a b c
    # O     a b c
    # X       a b c
    # X         a b c
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = Counter(s1)
        window = Counter(s2[:len(s1)])
        
        if window == target:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            window[s2[r]] += 1
            window[s2[l]] -= 1
            if window == target:
                return True
            l += 1

        return False

            


                
            
 