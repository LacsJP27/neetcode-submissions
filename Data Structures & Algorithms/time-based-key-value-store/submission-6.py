class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        vals = self.timeMap.get(key, [])
        vals.append((value, timestamp))
        self.timeMap[key] = vals

    def get(self, key: str, timestamp: int) -> str:

        vals = self.timeMap.get(key, [])

        return self.binarySearch(vals, timestamp)

    def binarySearch(self, vals, timestamp):
        l, r = 0, len(vals) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            val, time = vals[mid]
            if time <= timestamp:
                l = mid + 1
                res = val
            else:
                r = mid - 1
        return res
        
            
        
