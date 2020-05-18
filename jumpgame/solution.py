class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        prevPath = nums[0]
        for i in range(1, len(nums)):
            if prevPath <= 0:
                return False
            prevPath = max(prevPath-1 , nums[i])
        return True
