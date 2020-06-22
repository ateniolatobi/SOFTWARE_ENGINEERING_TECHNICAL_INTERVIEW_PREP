class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = -1 if (numerator * denominator) < 0 else 1
        numerator, denominator = abs(numerator), abs(denominator)
        res = numerator //  denominator
        res = str(res)
        rem = numerator % denominator
        denom, rem = str(denominator), str(rem)
        afterDec = ''
        haveSeen = {}
        start = ''
        ind = 0
        haveSeen[rem] = len(rem) + 1
        while int(rem) != 0:
            tempRem = rem
            while len(tempRem) < len(denom):
                tempRem += '0'
                
            if int(tempRem) < int(denom) and len(rem) < len(denom):
                numb = str(0)
                rem = tempRem
            elif int(tempRem) < int(denom):
                tempRem += '0'
                numb = str(int(tempRem) // int(denom))
                rem = str(int(tempRem) % int(denom))
            else:
                numb = str(int(tempRem) // int(denom))
                rem = str(int(tempRem) % int(denom))
                
            if rem in haveSeen:
                i =  haveSeen[rem]
                res += numb
                res = res[0:i] + '(' + res[i:] + ')'
                print('numb is ', rem)
                print('location is ', haveSeen[rem])
                break
            
            if ind == 0:
                res += '.'
                ind = len(res) + 1
            haveSeen[rem] = ind
            res += numb
            ind += 1
            
        
        print('res is ', res)
        print('afterDec is ', afterDec)
        print('start is ', start)
        print('has seen is ', haveSeen)
        return res if sign == 1 else '-' + res

        
        
        
        
            
            
        
