class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r, c = len(text1) + 1, len(text2) + 1
        mem = [[0 for j in range(c)] for i in range(r)]
        
        res = 0
        for i in range(1, r):
            for j in range(1, c):
                if text1[i-1] != text2[j-1]:
                    mem[i][j] = max(mem[i-1][j-1], mem[i-1][j], mem[i][j-1])
                else:
                    mem[i][j] =  mem[i-1][j-1] + 1
                res = max(res, mem[i][j])
        
        return res