class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        while L < R:
            if nums[L] < nums[R]:
                return nums[L]
            mid = (L+R) // 2

            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid
        return nums[L]

        

        