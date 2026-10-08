import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -1 * abs(x - y))
        
        if len(stones) == 0:
            return 0
        return -1 * stones[0]
        