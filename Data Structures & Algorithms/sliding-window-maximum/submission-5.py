import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def pop(heap):
            return -1 * heapq.heappop(heap)
        def push(heap, val):
            heapq.heappush(heap, -1 * val)
        def getMax(heap):
            return -1 * heap[0]
        ret = []
        heap = []
        counts = {}
        for idx in range(k):
            val = nums[idx]
            counts[val] = counts.get(val, 0) + 1
            push(heap, val)
        ret.append(getMax(heap))
        for R in range(k, len(nums)):
            toRemove = nums[R - k]
            counts[toRemove] -= 1
            push(heap, nums[R])
            counts[nums[R]] = counts.get(nums[R], 0) + 1

            while counts[getMax(heap)] == 0:
                pop(heap)
            ret.append(getMax(heap))
        return ret



    


        
        
        