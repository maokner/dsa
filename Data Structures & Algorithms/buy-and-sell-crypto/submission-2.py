class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0

        L = 0
        for R in range(len(prices)):
            ret = max(ret, prices[R] - prices[L])
            if prices[R] < prices[L]:
                L = R
        return ret
        