class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            # NUM PUSH
            if tok not in {'+', '-', '*', '/'}:
                stack.append(tok)
                continue
            # POP BA
            b = int(stack.pop())
            a = int(stack.pop())
            # APPLY
            if tok == '+':
                r = a + b
            elif tok == '-':
                r = a - b
            elif tok == '*':
                r = a * b
            else:
                r = a / b
            # RESULT PUSH
            stack.append(r)
        return int(stack[0])
        