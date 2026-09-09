class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        ret = 0

        while L < R:
            ret = max(ret, (R-L) * min(heights[R], heights[L]))
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return ret
        