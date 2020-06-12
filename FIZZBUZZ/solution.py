class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        out = []
        for i in range(1,n+1):
            if not i % 3 and not i % 5:
                out.append('FizzBuzz')
            elif not i % 3:
                out.append('Fizz')
            elif not i % 5:
                out.append('Buzz')
            else:
                out.append(str(i))
                
        return out
                
