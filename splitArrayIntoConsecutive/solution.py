class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        tail = collections.Counter()
        n = len(nums)
        
        for i in range(n):
            v = nums[i]
            v1 = v+1
            v2 = v+2
            if count[v] == 0:
                continue
            elif tail[v] > 0:
                tail[v+1] += 1
                tail[v] -= 1
            elif count[v1] > 0 and count[v2] > 0:
                count[v1] -= 1
                count[v2] -= 1
                tail[v2+1] += 1
            else:
                return False
            
            count[v] -= 1
        return True