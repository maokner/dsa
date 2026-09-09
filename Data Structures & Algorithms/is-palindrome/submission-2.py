class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            inc = False
            if not s[l].isalnum():
                l += 1
                inc = True
            if not s[r].isalnum():
                r -= 1
                inc = True
            if not inc:
                left = s[l]
                right = s[r]
                if left.isalpha():
                    left = left.lower()
                if right.isalpha():
                    right = right.lower()
                if left != right:
                    return False
                l += 1
                r -= 1
        return True
        