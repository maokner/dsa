class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        idx = nums[0]
        while nums[idx] != -1:
            new_idx = nums[idx]
            nums[idx] = -1
            idx = new_idx
        return idx

        