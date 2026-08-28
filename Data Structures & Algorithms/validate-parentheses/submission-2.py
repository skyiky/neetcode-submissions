from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if len(s) % 2 != 0:
            return False
        for c in s:
            if c == ')':
                if len(stack) > 0 and stack.pop() == "(":
                    continue
                else:
                    return False
            elif c == '}':
                if len(stack) > 0 and stack.pop() == "{":
                    continue
                else:
                    return False
            elif c == "]":
                if len(stack) > 0 and stack.pop() == "[":
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        