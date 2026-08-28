class Solution:
    # Sort the input list then fix smallest number, then converge two pointers to find the other two while skipping duplicates (re-use "Two Integer Sum II" approach).
    # i j . . . . k 
    # i . j . . . k
    # i . j . . k .
    # i . . j k . .
    # . i j . . . k
    # . i . j . . k
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        result = [] # alternative solution not requiring explicit duplicate handling uses a set of tuples.
        for i in range(len(nums)-2):
            if s[i] > 0:
                break
            
            if i > 0 and s[i] == s[i-1]: # optimization to skip redundant work and required to omit duplicates in the result
                continue

            l = i+1
            r = len(nums)-1
            while l < r:
                _sum = s[i] + s[l] + s[r]
                if _sum > 0:
                    r -= 1
                elif _sum < 0:
                    l += 1
                else:
                    result.append([s[i], s[l], s[r]]) # alt: result.add(tuple([s[i], s[l], s[r]]))
                    r -= 1
                    l += 1
                    while l < r and s[l] == s[l-1]: # optimization...
                        l += 1
                    while l < r and s[r] == s[r+1]: # optimization...
                        r -= 1
        return result # alt: [list(t) for t in result]


