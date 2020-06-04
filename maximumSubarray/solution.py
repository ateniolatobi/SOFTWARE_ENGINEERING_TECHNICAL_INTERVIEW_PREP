class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tempMax, maxSub = float('-inf'), float('-inf')
        for i in range(len(nums)):
            tempMax = max(tempMax + nums[i], nums[i])
            maxSub = max(maxSub, tempMax)
        return maxSub
