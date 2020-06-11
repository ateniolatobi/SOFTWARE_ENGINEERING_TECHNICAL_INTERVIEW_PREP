class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        summ = sum(A)
        T =  summ / 3
        if summ % 3 != 0:
            return False
        runSum = 0
        count = 0
        for i in range(len(A)):
            runSum += A[i]
            if runSum == T:
                # print('triggered for ', i)
                count += 1
                runSum = 0   
        if count >= 3:
            return True
        return False
                
                
