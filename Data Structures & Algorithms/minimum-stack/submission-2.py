class MinStack:

    def __init__(self):
        self.items = []
        

    def push(self, val: int) -> None:
        self.items.append(val)

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        temp = []
        minVal = self.items[-1]

        while len(self.items):
            minVal = min(self.items[-1], minVal)
            temp.append(self.items.pop())

        while len(temp):
            self.items.append(temp.pop())

        return minVal
