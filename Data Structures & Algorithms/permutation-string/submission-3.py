class Solution:
    # fixed size window
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord("a")] += 1
            freq2[ord(s2[i]) - ord("a")] += 1

        matches = sum(freq1[i] == freq2[i] for i in range(26))
        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # add right char
            i = ord(s2[r]) - ord("a")
            freq2[i] += 1
            
            if freq2[i] == freq1[i]:
                matches += 1
            elif freq2[i] - 1 == freq1[i]:
                matches -= 1

            # remove left char
            i = ord(s2[l]) - ord("a")
            freq2[i] -= 1

            if freq2[i] == freq1[i]:
                matches += 1
            elif freq2[i] + 1 == freq1[i]:
                matches -= 1
            
            l += 1
        
        return matches == 26


                
            
 