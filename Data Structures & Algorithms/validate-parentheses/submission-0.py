class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # MAP CLOSE
        pairs = {')':'(', '}':'{', ']':'['}
        # PUSH OR MATCH
        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        # RETURN NOT EMPTY
        return not stack
        