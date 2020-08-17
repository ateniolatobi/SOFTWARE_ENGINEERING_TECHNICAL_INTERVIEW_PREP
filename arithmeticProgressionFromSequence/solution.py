class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if not arr or len(arr) == 1:
            return True
        

        n = len(arr)
        arr = sorted(arr)
        
        diff = arr[1] - arr[0]
        for i in range(1,n):
            if arr[i] - arr[i-1] != diff:
                return False
        return True