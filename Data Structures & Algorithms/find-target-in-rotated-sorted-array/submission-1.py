class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(nums, target, L, R):
            while L <= R:
                mid = (L+R) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    R = mid - 1
                else:
                    L = mid + 1
            return -1

        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (L+R) // 2
            if nums[mid] == target:
                return mid
            inLeft = nums[mid] >= nums[L]
            if inLeft and target > nums[mid]:
                L = mid + 1
            elif inLeft and target < nums[mid]:
                if nums[L] <= target:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                #in right sorted portion
                if nums[mid] <= target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1

                    
        return -1
        
            

            


    
        