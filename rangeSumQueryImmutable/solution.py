class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.rundict = {}
        self.rundict[-1] = 0
        n = len(nums)
        for i in range(n):
            self.rundict[i] = self.rundict[i-1] + self.nums[i]
        

    def sumRange(self, i: int, j: int) -> int:
        
        return self.rundict[j] - self.rundict[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)