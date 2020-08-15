class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        # out = [1] * n
        outdict = {}
        longseq = 0
        for i in range(n):
            for j in range(0, i):
                diff = A[i] - A[j]
                if diff not in outdict:
                    outdict[diff] = [1] * n
                pointer = outdict[diff] 
                pointer[i] = max(pointer[i], pointer[j] + 1)
                longseq = max(longseq, pointer[i])
        # print(longseq)
        return longseq