from collections import OrderedDict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if k <= 0 or not nums:
            return False

        
        
        buckets = OrderedDict()
        
        for num in nums:
            if num in buckets:
                return True
            buckets[num] = None 
            if len(buckets) == k+1:
                buckets.popitem(last = False)
                
        return False
        
        