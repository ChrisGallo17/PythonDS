class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = []
        self.ht = {}

        for i in range(len(nums)):
            if nums[i] not in self.ht:
                self.queue.append(nums[i])
                self.ht[nums[i]] = False
            else:
                self.ht[nums[i]] = True

        while self.queue != [] and self.ht[self.queue[0]] == True:
            self.queue.pop(0)

    def showFirstUnique(self) -> int:
        if self.queue == []:
            return -1
        return self.queue[0]

    def add(self, value: int) -> None:
        if value not in self.ht:
            self.queue.append(value)
            self.ht[value] = False
        else:
            self.ht[value] = True

        while self.queue != [] and self.ht[self.queue[0]] == True:
            self.queue.pop(0)


f = FirstUnique([2, 3, 5])
print(f.showFirstUnique())
print(f.add(5))
print(f.showFirstUnique())
print(f.add(2))
print(f.showFirstUnique())
print(f.add(3))
print(f.showFirstUnique())
