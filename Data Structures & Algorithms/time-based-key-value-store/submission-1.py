class TimeMap:

    def __init__(self):
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append([value, timestamp])
        else:
            self.dict[key] = [[value, timestamp]]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        search = self.dict[key]
        L = 0
        R = len(search) - 1
        best = ""
        while L <= R:
            mid = (L+R) // 2

            if search[mid][1] > timestamp:
                R = mid - 1
            else:
                best = search[mid][0]
                L = mid + 1
        return best
        
