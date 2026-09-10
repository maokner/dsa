class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        counts1 = [0] * 26
        counts2 = [0] * 26
        for c in s1:
            counts1[ord(c) - ord('a')] += 1
        
        for i in range(len(s1)):
            counts2[ord(s2[i]) - ord('a')] += 1
        if counts2 == counts1:
            return True

        
        for R in range(len(s1), len(s2)):
            counts2[ord(s2[R]) - ord("a")] += 1
            counts2[ord(s2[R - len(s1)]) - ord('a')] -= 1

            if counts2 == counts1:
                return True
        return False
        
        