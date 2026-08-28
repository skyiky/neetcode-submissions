class MinStack:
    # Key Idea: Stack entry = (value, minimum so far)
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = self.stack[-1][1] if self.stack else val
        new_min = min(val, current_min)
        self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
