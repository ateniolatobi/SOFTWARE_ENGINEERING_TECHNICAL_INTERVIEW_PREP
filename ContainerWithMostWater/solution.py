class Solution:
    def calcArea(self, height, start, end):
        return min(height[start], height[end]) * (end - start)
    
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxArea = 0
        while start < end:
            area = self.calcArea(height, start, end)	
            maxArea = max(area, maxArea)
            minVertix = min(height[start], height[end])
            if minVertix == height[start]:
                start += 1
            else:
                end -= 1
        return maxArea
            
