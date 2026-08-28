class Solution:
    # ["4", "13", "5", "/", "+"]
    # 4 + (13 / 5) = 6
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {'+', '-', '*', '/'}:
                stack.append(int(t))
                continue
            
            arg2 = stack.pop()
            arg1 = stack.pop()

            match t:
                case '+':
                    stack.append(arg1 + arg2)
                case '-':
                    stack.append(arg1 - arg2)
                case '*':
                    stack.append(arg1 * arg2)
                case '/':
                    stack.append(int(arg1 / arg2))
        return stack[0]
                    
