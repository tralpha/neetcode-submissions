class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            # NUM PUSH
            if tok not in {"*", "/", "+", "-"}:
                stack.append(int(tok))
                continue
            # POP BA
            b = stack.pop()
            a = stack.pop()    
            # APPLY
            if tok == "*":
                res = int(a * b)
            elif tok == "+":
                res = int(a + b)
            elif tok == "-":
                res = int(a - b)
            else:
                res = int(a / b)
            # RES PUSH
            stack.append(res)
        return stack[0]
        