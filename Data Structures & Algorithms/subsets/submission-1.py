class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        def helper(idx, currList):
            if idx == len(nums):
                return
            temp = currList + [nums[idx]]
            self.res.append(temp)
            helper(idx + 1, temp)
            helper(idx + 1, currList)
        
        helper(0, [])

        return self.res

        