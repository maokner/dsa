class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = [] # [[temp, idx]]
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, replIdx = stack.pop()
                ret[replIdx] = idx - replIdx
            stack.append([temp, idx])
        
        return ret