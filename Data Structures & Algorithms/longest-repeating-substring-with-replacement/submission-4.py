class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        seen = {}
        ret = 0
        maxInSequence = 0

        for R, c in enumerate(s):
            seen[c] = seen.get(c, 0) + 1
            maxInSequence = max(maxInSequence, seen[c])
            while (R - L + 1) > (maxInSequence + k):
                seen[s[L]] -= 1
                L += 1
            ret = max(ret, R - L + 1)
        return ret


        