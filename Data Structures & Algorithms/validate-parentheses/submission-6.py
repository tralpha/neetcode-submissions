class Solution:
    def isValid(self, s: str) -> bool:
        # MAP CLOSE
        pairs = {'}':'{', ']':'[', ')':'('}
        stack = []
        for c in s:
            # PUSH OR MATCH
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        # NOT EMPTY
        return not stack