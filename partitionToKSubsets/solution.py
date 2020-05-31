class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        elemSum = sum(nums)
        if elemSum % k != 0:
            return False
        T = elemSum // k
        nums.sort()
        def helper(groups):
            if not nums:
                return True
            v = nums.pop()
            for i in range(len(groups)):
                if groups[i] + v <= T:
                    groups[i] += v
                    if helper(groups):
                        return True
                    groups[i] -= v
            nums.append(v)
            return False
        
        
        return helper([0] * k)
