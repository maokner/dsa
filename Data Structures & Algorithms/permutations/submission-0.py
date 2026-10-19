class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtrack(left, curr):
            if len(left) == 0:
                self.res.append(curr.copy())
                return
            for idx in list(left):
                curr.append(nums[idx])
                left.remove(idx)
                backtrack(left, curr)
                left.add(idx)
                curr.pop()
        left = set([i for i in range(len(nums))])
        backtrack(left, [])

        return self.res
