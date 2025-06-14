import random

class RandomizedSet:

    def __init__(self):
        self.hashmap = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap.add(val)
            return True
        return False
        
        

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        self.hashmap.remove(val)
        return True
        

    def getRandom(self) -> int:
        randomm = random.randint(0, len(self.hashmap)-1)
        hashmapList = list(self.hashmap)
        return hashmapList[randomm]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()