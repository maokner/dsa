class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1 for _ in range(len(nums))]
        rightProducts = [1 for _ in range(len(nums))]

        #calculate product of all items to the left
        for idx in range(1, len(nums)):
            leftProducts[idx] = leftProducts[idx - 1] * nums[idx - 1]
        for idx in range(len(nums) - 2, -1, -1):
            rightProducts[idx] = rightProducts[idx + 1] * nums[idx + 1]
        
        return [leftProducts[i] * rightProducts[i] for i in range(len(nums))]

        