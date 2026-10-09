import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0] ** 2 + point[1] **2
            heap.append([dist, point])
        heapq.heapify(heap)
        ret = []

        while k > 0:
            ret.append(heapq.heappop(heap)[1])
            k -= 1
        return ret
