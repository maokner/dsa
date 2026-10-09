import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        queue = deque()
        seen = {}
        for task in tasks:
            seen[task] = seen.get(task, 0) - 1
        heap = list(seen.values())
        heapq.heapify(heap)

        t = 0
        while heap or queue:
            t += 1
            if heap:
                curr = heapq.heappop(heap)
                if curr != -1:
                    queue.append([curr + 1, t + n])
            if queue:
                if queue[0][1] == t:
                    heapq.heappush(heap, queue.popleft()[0])
        

        return t
        
        