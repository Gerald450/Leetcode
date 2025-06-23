class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        if val not in self.numMap:
            self.numList.append(val)
            self.numMap[val] = (len(self.numList) - 1)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.numMap:
            idx = self.numMap[val]
            last = self.numList[-1]
            self.numList[idx] = last
            self.numList.pop()
            self.numMap[last] = idx
            del self.numMap[val]
            return True
        return False 
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()