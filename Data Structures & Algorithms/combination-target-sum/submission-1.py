class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        
        def helper(idx, currList, currSum):
            if currSum == target:
                self.res.append(currList)
                return
            if currSum > target:
                return
            else:
                if idx < len(nums):
                    temp = currList[:]
                    temp.append(nums[idx])
                    helper(idx, temp, currSum + nums[idx])

                    helper(idx + 1, currList, currSum)
        
        helper(0, [], 0)
    
        return self.res
    
