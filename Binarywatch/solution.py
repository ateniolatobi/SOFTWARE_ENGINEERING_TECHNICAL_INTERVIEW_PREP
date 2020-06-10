class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        
        
        res = set()
        def helper(minarr, hourarr, hour, minutes, total):
            if hour > 11 or minutes > 59:
                return 
            
            if total == num:
                hour = str(hour)
                if minutes < 10:
                    minutes = '0' + str(minutes)
                time = '{0}:{1}'.format(hour, minutes)
                res.add(time)
                return
            
            for i in range(len(hourarr)):
                if total < num and hourarr[i] == 0:
                    hourarr[i] = 1
                    hour += 2 ** i
                    helper(minarr, hourarr, hour, minutes, total+1)    
                    hourarr[i] = 0
                    hour -= 2 ** i
                    
                
                
            for j in range(len(minarr)):
                if total < num and minarr[j] == 0:
                    minarr[j] = 1
                    minutes += 2 ** j
                    helper(minarr, hourarr, hour, minutes, total+1)
                    minutes -= 2 ** j
                    minarr[j] = 0
            return 
        
        
        
        helper([0,0,0,0,0,0], [0,0,0,0], 0, 0, 0)
        # print(len(res))
        return list(res)
