class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:
            return False
        self.map[self.list[-1]] = self.map[val]
        self.list[-1], self.list[self.map[val]] = self.list[self.map[val]], self.list[-1] 
        self.list.pop()
        self.map.pop(val)
        return True
                                                      

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not self.list:
            return 
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
