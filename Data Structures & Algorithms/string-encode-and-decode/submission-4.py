class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + ";"
            ret += s
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        idx = 0
        currNum = ""
        while idx < len(s):
            if s[idx] == ";":
                currLen = int(currNum)
                ret.append(s[idx+1:idx+1+currLen])
                currNum = ""
                idx += (1+currLen)
            else:
                currNum += s[idx]
                idx += 1
        return ret
