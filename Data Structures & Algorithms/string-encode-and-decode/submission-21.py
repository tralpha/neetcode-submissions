class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            # find delimiter
            j = s.index("#", i)
            # length
            length = int(s[i:j])
            # slice
            res.append(s[j + 1: j + 1 + length])
            # jump
            i = j + 1 + length
        return res


        
