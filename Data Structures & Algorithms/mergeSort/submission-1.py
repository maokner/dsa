# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        p1 = self.mergeSort(pairs[:len(pairs) // 2])
        p2 = self.mergeSort(pairs[len(pairs) // 2:])

        i, j = 0, 0

        ret = []

        while (i < len(p1)) and (j < len(p2)):
            if p1[i].key > p2[j].key:
                ret.append(p2[j])
                j += 1
            else:
                ret.append(p1[i])
                i += 1
        
        while i < len(p1):
            ret.append(p1[i])
            i += 1
        while j < len(p2):
            ret.append(p2[j])
            j += 1

        return ret
            
