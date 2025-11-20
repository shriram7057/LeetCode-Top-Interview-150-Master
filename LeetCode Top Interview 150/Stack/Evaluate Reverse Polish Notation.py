class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(t))
        return stack[-1]
