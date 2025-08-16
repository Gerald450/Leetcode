class Trie:

    def __init__(self):
        self.arr = []
        

    def insert(self, word: str) -> None:
        self.arr.append(word)
        

    def search(self, word: str) -> bool:
        if word in self.arr:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        for word in self.arr:
            if word[:n] == prefix:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)