class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Parse #
            j = s.index("#", i)
            # Find length
            length = int(s[i:j])
            # Slice
            res.append(s[j+1:j+1+length])
            # Jump
            i = j + 1 + length
        return res


        
