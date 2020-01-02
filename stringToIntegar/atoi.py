class Solution:
    def myAtoi(self, str: str) -> int:
        min_int, max_int = [-2147483648, 2147483647]
        # str = "+1"
        str = str.strip(" ")
        if not str:
            return 0
        sign = ""
        if str[0] == "-":
            sign = "-"
            str = str[1:len(str)]
        elif str[0] == "+":
            sign = ""
            str = str[1:len(str)]
        if not str or not str[0].isnumeric():
            return 0
        num = ""
        for c in str:
            if c.isnumeric():
                num += c
                continue
            break
        num = int(sign + num)
        num = max(num, min_int)
        num = min(num, max_int)
        return num
                
            
        