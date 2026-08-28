class Solution:
    # There are two optimal approaches:
    # Forward scan: stack holds past days still waiting for a warmer day; the current temperature resolves them.
    # Reverse scan: stack holds useful future-day candidates; smaller/equal candidates are removed.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            stack.append(i)
        return result
            
            
                