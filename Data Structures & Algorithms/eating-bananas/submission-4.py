class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(piles, rate):
            ret = 0
            for pile in piles:
                ret += pile // rate
                if pile % rate != 0:
                    ret += 1
            return ret

        max_rate = max(piles)
        L = 1
        R = max_rate
        curmin = R
        while L <= R:
            mid = (L + R) // 2
            if hours(piles, mid) <= h:
                curmin = mid
                R = mid - 1
            else:
                L = mid + 1
        return curmin


        
        


        