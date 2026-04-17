class MedianFinder:

    def __init__(self):
        self.data_stream = []

    def addNum(self, num: int) -> None:
        self.data_stream.append(num)

    def findMedian(self) -> float:
        self.data_stream.sort()
        mid = len(self.data_stream) // 2

        if len(self.data_stream) & 1 :
            return self.data_stream[mid]
        else:
            return (self.data_stream[mid] + self.data_stream[mid - 1]) / 2
        