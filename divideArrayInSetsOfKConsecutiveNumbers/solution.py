from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        valsdict = Counter(nums)
        
        # print(valsdict)
        
        
        
        tots = 0
        nums.sort()
        print(nums)
        for i in range(n):
            val = nums[i]
            if valsdict[val-1] > 0 or valsdict[val] <= 0:
                continue
            count = 1
            valsdict[val] -= 1
            while valsdict[val+1] > 0 and count < k:
                val = val + 1
                valsdict[val] -= 1
                count += 1
                
            if count == k:
                tots += 1
        if tots * k == n:
            return True
        return False