class Solution:
    def searchLeftIndex(self, arr, target, start, end):
        mid = int((start + end) / 2)
        if (end - start) < 1:
            return -1
        # print("left mid is ", mid)
        if arr[mid] == target and ((mid -1) < 0 or arr[mid-1] != target):
            return mid
        
        if target > arr[mid]:
            # print("went here")
            return self.searchLeftIndex(arr, target, mid + 1, end)
        else:
            return self.searchLeftIndex(arr, target, start, mid)
        
    def searchRightIndex(self, arr, target, start, end):
        mid = int((start + end) / 2)
        # print("The arr is ", arr[start:end+1])
        # print("The mid is ", mid)
        if (end - start) < 1:
            return -1
        if arr[mid] == target and ((mid + 1) >= len(arr) or arr[mid+1] != target):
            return mid
        
        if target < arr[mid]:
            return self.searchRightIndex(arr, target, start, mid)
        else:
            return self.searchRightIndex(arr, target, mid + 1, end)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # nums = [2, 2]
        # target = 3
        if not nums:
            return [-1, -1]
        if len(nums) == 1 and target in nums:
            return [0, 0]
        left = self.searchLeftIndex(nums, target, 0, len(nums))
        start = 0
        if left != -1:
            start = left
        right = self.searchRightIndex(nums, target, start, len(nums))
        return [left, right]


