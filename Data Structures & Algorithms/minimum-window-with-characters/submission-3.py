class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c1 = {}
        c2 = {}
        ret = ""
        for c in t:
            c1[c] = c1.get(c, 0) + 1
        numUnique = len(c1)
        
        numCovered = 0
        L = 0
        for R, c in enumerate(s):
            c2[c] = c2.get(c, 0) + 1
            if c2[c] == c1.get(c, float('inf')):
                numCovered += 1
            while numCovered >= numUnique:
                #we fully cover all chars in s
                if ret == "" or len(ret) > (R - L + 1):
                    ret = s[L:R+1]
                toRemove = s[L]
                if c2[toRemove] == c1.get(toRemove, float("inf")):
                    numCovered -= 1
                c2[toRemove] -= 1
                L += 1
        return ret

            
        