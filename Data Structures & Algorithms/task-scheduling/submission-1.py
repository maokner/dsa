import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        counts = {}
        notReady = deque()
        for task in tasks:
            counts[task] = counts.get(task, 0) - 1
        for key in counts:
            heapq.heappush(heap, counts[key])
        
        time = 0
        while heap or notReady:
            time += 1
            while notReady and time > notReady[0][1]:
                heapq.heappush(heap, notReady.popleft()[0])
    
            if heap:
                curr = heapq.heappop(heap)
                if curr != -1:
                    notReady.append([curr + 1, time + n])
            
        

        return time
        