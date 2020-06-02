class Solution:
    def countAndSay(self, n: int) -> str:
        # n = 5
        if n == 1:
            return '1'
        
        say = '1'
        for i in range(n-1):
            curr = say[0]
            count = 0
            futSay = []
            for j in range(len(say)):
                if say[j] == curr:
                    count += 1
                else:
                    futSay.append(str(count))
                    futSay.append(curr)
                    curr = say[j]
                    count = 1
                    
                if j == (len(say)-1):
                    futSay.append(str(count))
                    futSay.append(curr)
            say = ''.join(futSay)
            # print('for ', i, ' say is ', say)
            
        return say
