class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums, target):
            L = 0
            R = len(nums) - 1
            while L <= R:
                mid=( L + R) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] > target:
                    R = mid - 1
                else:
                    L = mid + 1
            return False
        
        L = 0
        R = len(matrix)
        while L <= R:
            mid = (L + R) // 2
            if matrix[mid][0] <= target:
                if mid == len(matrix) - 1 or matrix[mid+1][0] > target:
                    return binarySearch(matrix[mid], target)
                else:
                    L = mid + 1
            else:
                if mid == 0:
                    return False
                R = mid - 1
        
                


        