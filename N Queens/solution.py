class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        
        out = []
        rows, cols = [set() for i in range(n)], [set() for i in range(n)]
        diag1, diag2 = [set() for i in range(2*n-1)], [set() for i in range(2*n-1)]
        board = [['.' for j in range(n)] for i in range(n)]
        # print(board)
        
        def helper(r, c, count):
            # print('count ', count)
            if count == n:
                # print('count cuaght')
                out.append([''.join(board[i]) for i in range(n)])
                # print(out[-1])
                return
            if c == n:
                return helper(r+1, 0, count)
            if r == n:
                return  
            if board[r][c] != 'Q' and 'Q' not in rows[r] and 'Q' not in cols[c] and 'Q' not in diag1[r+c] and 'Q' not in  diag2[(r-c)+(n-1)]:
                board[r][c] = 'Q'
                rows[r].add('Q')
                cols[c].add('Q')
                diag1[r+c].add('Q')
                diag2[(r-c)+(n-1)].add('Q')
                
                helper(r, c+1, count+1)
                
                board[r][c] = '.'
                rows[r].remove('Q')
                cols[c].remove('Q')
                diag1[r+c].remove('Q')
                diag2[(r-c)+(n-1)].remove('Q')
            
            return helper(r, c+1, count)
        
        helper(0,0,0)
        return out
            
            
