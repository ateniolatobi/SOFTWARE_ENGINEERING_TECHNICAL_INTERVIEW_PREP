class Solution:
    def numDecodings(self, s: str) -> int:
        # s = '22106'
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if i > 1 and 0 < (int(s[i-1]) + int(s[i-2]) * 10) <= 26 and s[i-2] != '0':
                dp[i] += dp[i-2]
                
            if s[i-1] != '0':
                dp[i] += dp[i-1]

                
        return dp[len(s)]
            
