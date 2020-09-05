from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        cache = DefaultDict(int)
        maxcount = 1
        n = len(arr)
        for i in range(n):
            v = arr[i]
            if cache[v-difference] <= 0:
                cache[v] = 1
            else:
                cache[v] = max(cache[v], cache[v-difference] + 1)
            
            maxcount = max(maxcount, cache[v])
            
        return maxcount