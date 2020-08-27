class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertTime(time):
            hour, mins = time.split(':')
            return int(hour) * 60 + int(mins)
        
        
        timePoints.sort()
        n = len(timePoints)
        ans = float('inf')
        for i in range(n):
            
            j = (i+1) % n
            diff = (convertTime(timePoints[j]) - convertTime(timePoints[i])) % 1440
            
            ans = min(ans, diff)
            
        return ans
            