class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        map = [[1 for j in range(m)]for i in range(n)]
        # print(map)
        for i in range(1, n):
            for j in range(1, m):
                map[i][j] = map[i-1][j] + map[i][j-1]
#         map[1][2] = 4  
        
#         print(map)

        return map[n-1][m-1]
        
