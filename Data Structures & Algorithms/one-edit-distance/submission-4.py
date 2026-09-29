class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        if abs(len(s) - len(t)) > 1:
            return False
        
        while p1 < len(s) and p2 < len(t):
            c1 = s[p1]
            c2 = t[p2]
            if c1 != c2:
                if len(s) == len(t):
                    #must simply replace character
                    if s[p1+1:] == t[p2+1:]:
                        return True
                    return False
                else:
                    if len(t) > len(s):
                        if s[p1:] ==  t[p2+1:]:
                            return True
                        return False 
                        
                    else:
                        return s[p1+1:] == t[p2:]
            else:
                p1 += 1
                p2 += 1
        if abs(len(t) - len(s)) == 1:
            return True
        return False