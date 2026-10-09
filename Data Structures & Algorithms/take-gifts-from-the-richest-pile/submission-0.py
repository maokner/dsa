import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        edit = [-gift for gift in gifts]
        heapq.heapify(edit)
        
        for _ in range(k):
            curr = -1 * heapq.heappop(edit)
            heapq.heappush(edit, -1 * math.floor(curr ** 0.5))
        return -1 * sum(edit)