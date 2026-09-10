class Solution:
    def trap(self, height: List[int]) -> int:
        ret = 0
        maxLeft = [0 for _ in range(len(height))]
        maxRight = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i+1])
        
        for i in range(len(height)):
            ret += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        return ret