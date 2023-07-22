# import collections

# class TimeMap:
#     def __init__(self):
#         self.data = collections.defaultdict(list)

#     def set(self, key, value, timestamp):
#         self.data[key].append((timestamp, value))

#     def get(self, key, timestamp):
#         if key not in self.data:
#             return ""

#         values = self.data[key]

#         # Linear search to find the value associated with the largest timestamp_prev
#         for i in range(len(values) - 1, -1, -1):
#             if values[i][0] <= timestamp:
#                 return values[i][1]

#         return ""

import collections

class TimeMap:
    def __init__(self):
        self.data = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.data.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)