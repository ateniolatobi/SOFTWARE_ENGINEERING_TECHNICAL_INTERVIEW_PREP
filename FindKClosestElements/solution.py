class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        n = len(arr)
        diff = float('inf')
        pivot = 0
        for i in range(n):
            v = arr[i]
            if abs(x-v) < diff:
                diff =abs(x-v)
                pivot = i
        # print('pivot is ', pivot)
        start = end = pivot
        out = []
        count = 0
        while (start >= 0 or end < n) and count < k:
            print((start,end))
            count += 1
            if start == end:
                out.append(arr[start])
                start -= 1
                end += 1
                continue
            left = float('inf')
            if start >= 0:
                left = arr[start]
            right = float('inf')
            if end < n:
                right = arr[end]
            # print('left is ', abs(x-left))
            # print('right is ', abs(x-right))
            if abs(x-left) <= abs(x-right):
                out.append(left)
                start -= 1
            else:
                out.append(right)
                end += 1
        return sorted(out)
      
            
            