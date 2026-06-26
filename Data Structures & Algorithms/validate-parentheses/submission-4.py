class Solution:
    def isValid(self, s: str) -> bool:
        # MAP CLOSE
        pairs = {'}':'{', ')':'(', ']':'['}
        stack = []
        # PUSH OR MATCH
        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        # RETURN NOT EMPTY
        return not stack
