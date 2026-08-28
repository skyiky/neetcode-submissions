class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # (value, index)
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                result[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return result
            
            
                