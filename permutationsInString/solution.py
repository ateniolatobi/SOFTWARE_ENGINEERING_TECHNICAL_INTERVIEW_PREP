class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        g = {}
        for c in s1:
            g[c] = g.get(c,0) + 1
        
        
        count = 0
        start = end = 0
        n = len(s2)
        movedict = {}
        while end < n:
            # movedict[s2[end]] = movedict.get(s2[end], 0) + 1
            c = s2[end]
            if c in g:
                movedict[c] = movedict.get(c, 0) + 1
                if movedict[c] == g[c]:
                    count += 1
            while count >= len(g):
                if (end - start + 1) == len(s1):
                    return True
                c = s2[start]
                if c in movedict:
                    movedict[c] -= 1
                    if movedict[c] == (g[c] - 1):
                        count -= 1
                start += 1
            end += 1
        return False
            
        