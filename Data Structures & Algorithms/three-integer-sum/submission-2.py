class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(L, numbers, target):
            ret = []
            R = len(numbers) - 1
            while L < R:
                if numbers[L] + numbers[R] == target:
                    ret.append([numbers[L], numbers[R], -1 * target])
                    left = numbers[L]
                    while L < R and numbers[L] == left:
                        L += 1
                    R -= 1
                elif numbers[L] + numbers[R] > target:
                    R -= 1
                else:
                    L += 1
            return ret
        nums = sorted(nums)
        ret = []
        seen = set()
        for idx, num in enumerate(nums):
            if num > 0:
                break
            if num not in seen:
                pairs = twoSum(idx+1, nums, -1 * num)
                ret.extend(pairs)  
                seen.add(num)
        return ret            

    
        