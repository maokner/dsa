class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def makeFreqTable(inStr: str):
            counts = [0 for _ in range(26)]
            for c in inStr:
                loc = ord(c) - ord('a')
                counts[loc] += 1
            return tuple(counts)
        
        anagrams = {}
        for s in strs:
            freq = makeFreqTable(s)
            if freq in anagrams:
                anagrams[freq].append(s)
            else:
                anagrams[freq] = [s]
        ret = []
        for key in anagrams:
            ret.append(anagrams[key])
        return ret