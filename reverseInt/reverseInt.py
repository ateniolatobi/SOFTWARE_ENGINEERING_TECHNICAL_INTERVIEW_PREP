class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        min, max = (-2**31, 2**31 - 1)
        val = str(x)
        sign = ""
        if val[0] == "-":
            sign = val[0]
            val = val[1:len(val)]
        val = val[::-1].lstrip("0")
        if len(val) > 10:
            return 0
        val = sign + val
        if (int(val) > min) and (int(val) < max):
            return val
        return 0