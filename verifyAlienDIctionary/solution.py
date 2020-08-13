class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def compare(lessword, largeword):
            startless, startlarge = 0, 0
            nless, nlarge = len(lessword), len(largeword)
            while startless < nless and startlarge < nlarge:
                cless, clarge = lessword[startless], largeword[startlarge]
                oless, olarge = d[cless], d[clarge]
                if olarge < oless:
                    return False
                elif oless < olarge:
                    return True
                startless += 1
                startlarge += 1
            if startless >= nless:
                return True
            return False
                
        
        d = {}
        norder = len(order)
        for i in range(norder):
            c = order[i]
            d[c] = i
            
        nwords = len(words)
        for i in range(1,nwords):
            lessword = words[i-1]
            largeword = words[i]
            if not compare(lessword, largeword):
                return False
        return True