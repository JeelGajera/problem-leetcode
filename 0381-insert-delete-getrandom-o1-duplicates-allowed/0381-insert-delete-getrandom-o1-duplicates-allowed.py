import random

class RandomizedCollection:

    def __init__(self):
        self.elems = []
        self.count = defaultdict(int)

    def insert(self, val: int) -> bool:
        self.elems.append(val)
        self.count[val] += 1
        return self.count[val] == 1
        
    def remove(self, val: int) -> bool:
        if val not in self.elems:
            return False

        self.elems.remove(val)
        self.count[val] -= 1
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.elems)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()