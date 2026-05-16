class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + "\x00" + s
        return res


    def decode(self, s: str) -> List[str]:
        strs = s.split("\x00")
        res = strs[1:]
        return res




        
