class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        out = []
        temp = [0]
        while temp:
            val = temp.pop()
            if 1<= val <= n:
                out.append(val)
            val = val * 10
            for i in range(9,-1,-1):
                if val == 0 and i == 0:
                    continue
                tempval = val + i
                if tempval > n:
                    continue
                temp.append(tempval)
        return out