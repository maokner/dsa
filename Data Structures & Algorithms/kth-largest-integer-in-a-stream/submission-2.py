import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.data = []
        self.size = 0
        self.k = k
        for num in nums:
            if self.size >= k:
                if num > self.data[0]:
                    heapq.heappop(self.data)
                    heapq.heappush(self.data, num)
            else:
                heapq.heappush(self.data, num)
                self.size += 1


    def add(self, val: int) -> int:
        if self.size < self.k:
            heapq.heappush(self.data, val)
            self.size += 1
        elif val > self.data[0]:
            heapq.heappop(self.data)
            heapq.heappush(self.data, val)
        return self.data[0]
        
