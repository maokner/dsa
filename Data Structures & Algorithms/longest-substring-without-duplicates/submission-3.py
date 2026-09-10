class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = {}
        ret = 0
        l = 0
        for r, c in enumerate(s):
            counts[c] = counts.get(c, 0) + 1

            while counts[c] > 1:
                counts[s[l]] -= 1
                l += 1
            
            ret = max(ret, r - l +1)
        return ret
        