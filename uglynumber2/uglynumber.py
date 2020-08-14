import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        
        heap = []
        res = [1]
        
        heap.append((2,0,2))
        heap.append((3,0,3))
        heap.append((5,0,5))
        
        
        
        while n > 1:
            
            multi, ind, factor = heapq.heappop(heap)
            
            if multi != res[-1]:
                res.append(multi)
                n -= 1
            ind += 1
            multi = factor * res[ind]
            form = ((multi, ind, factor))
            heapq.heappush(heap, form)
            
        return res[-1]