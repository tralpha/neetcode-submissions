class Solution:
    def isPalindrome(self, s: str) -> bool:
        # INIT LR
        L, R = 0, len(s) - 1
        while L < R:
            # SKIP JUNK
            while L < R and not s[L].isalnum():
                L += 1
                continue
            while L < R and not s[R].isalnum():
                R -= 1
                continue
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True
        