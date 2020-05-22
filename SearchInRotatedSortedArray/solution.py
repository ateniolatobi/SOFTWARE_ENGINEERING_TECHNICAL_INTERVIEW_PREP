class Solution:
    def bts(self, start, end, target, nums):
        mid = int((start + end) / 2)
        # print("start is {0} and end is {1} and mid is {2}".format(start, end, mid))
        if nums[mid] == target:
            return mid
        if (end - start) <= 1:
            return -1
        if nums[start] < nums[mid]:
            if target >= nums[start] and target <= nums[mid]:
                return self.bts(start, mid, target, nums)
            else:
                return self.bts(mid, end, target, nums)
        else:
            if target >= nums[mid] and target <= nums[end - 1]:
                return self.bts(mid, end, target, nums)
            else:
                return self.bts(start, mid, target, nums)
    def search(self, nums: List[int], target: int) -> int:
        # nums = [1, 3]
        # target = 1
        if not nums:
            return -1
        return self.bts(0, len(nums), target, nums)
        
 
