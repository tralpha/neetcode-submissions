class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # NUM PUSH
        for tok in tokens:
            if tok not in {"*", "+", "/", "-"}:
                stack.append(int(tok))
                continue
            # POP B A
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
        
        