class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) - k
        
        def helper(arr, start, end):
            leader, follower = start, start
            targ = end - 1
            
            while leader < targ:
                if arr[leader] <= arr[targ]:
                    arr[leader], arr[follower] = arr[follower], arr[leader]
                    follower += 1
                leader += 1
            arr[targ], arr[follower] = arr[follower], arr[targ]
            if follower == k:
                return arr[k]
            elif k < follower:
                return helper(arr, start, follower)
            return helper(arr, follower+1, end)
        
        return helper(nums, 0, len(nums))
                    
