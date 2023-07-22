import collections

class TimeMap:
    def __init__(self):
        self.data = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.data[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.data:
            return ""

        values = self.data[key]

        # Linear search to find the value associated with the largest timestamp_prev
        for i in range(len(values) - 1, -1, -1):
            if values[i][0] <= timestamp:
                return values[i][1]

        return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)