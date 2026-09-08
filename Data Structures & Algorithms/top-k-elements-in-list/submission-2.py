from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        buckets = defaultdict(set)
        for num in nums:
            if num in counts:
                buckets[counts[num]].remove(num)
            counts[num] += 1
            buckets[counts[num]].add(num)
        ret = []
        added = 0
        for frequency in range(len(nums), -1, -1):
            ret.extend(num for num in buckets[frequency])
            added += len(buckets[frequency])
            if added == k:
                return ret
        return ret

                
        