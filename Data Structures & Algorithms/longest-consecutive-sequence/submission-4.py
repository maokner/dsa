class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ret = 0
        for num in nums:
            if num - 1 not in nums: #valid start
                currLen = 1
                while num + currLen in nums:
                    currLen += 1
                
                ret = max(ret, currLen)
        return ret
