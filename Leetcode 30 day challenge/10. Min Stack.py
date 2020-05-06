class MinStack:

    def __init__(self):
        self.items = []
        self.min = []

    def push(self, x: int) -> None:
        self.items.append(x)
        if len(self.min) == 0 or x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        if self.min[-1] == self.items.pop():
            self.min.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
