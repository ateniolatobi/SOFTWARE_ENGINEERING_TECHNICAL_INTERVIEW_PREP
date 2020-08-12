class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        
#         minimize distance
#         maximize sum
        
        m = M = 0
        
        n = len(A)
        for i in range(1,n):
            m = max(m, A[i-1] + i-1)
            M = max(M, m + A[i] - i)
            
        return M
