class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = {}
        duplicates = 0
        ret = 0
        L = 0
        for R in range(len(s)):
            c = s[R]
            if c not in counts:
                counts[c] = 0
            if counts[c] == 1:
                duplicates += 1
            if duplicates != 1:
                ret = max(ret, R - L + 1)

            counts[c] += 1
            if counts[c] != 1:
                #duplicate found
                while duplicates != 0:
                    toRemove = s[L]
                    if counts[toRemove] == 2:
                        duplicates -= 1
                        counts[toRemove] -= 1
                    else:
                        counts[toRemove] -= 1
                    L += 1
        return ret
            
                
            


        