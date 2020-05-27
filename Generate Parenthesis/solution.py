class Solution:
    
    def getParenthesis(self, left, right, temp, output):
        if right < left:
            return
        if right == 0 and left == 0:
            output.append(''.join(temp))
            return
        
        if left > 0:
            temp.append('(')
            self.getParenthesis(left-1, right, temp[:], output)
            temp.pop()
        
        if right > 0:
            temp.append(')')
            self.getParenthesis(left, right-1, temp[:], output)
            temp.pop()
            
        
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        output = []
        self.getParenthesis(n, n, [], output)
        return output
        
