class Solution:
    def getMaxLength(self, arr, start, end):
        palin = ""
        while (start >= 0) and (end < len(arr)):
            if arr[start] != arr[end]:
                break
            if len(arr[start:end+1]) > len(palin):
                palin = arr[start:end+1]
            start -= 1
            end += 1
        return palin
    
    
    def longestPalindrome(self, s: str) -> str:
        maxArr = ""
        for i in range(len(s)):
            len1 = self.getMaxLength(s, i, i)
            len2 = self.getMaxLength(s, i, i+1)
            maxArr = max(len1, len2, maxArr, key=len)
            # maxArr = len1 if maxLen == len(len1) else len2 if maxLen ==  len(len2) else maxArr
            # if s[i] == 'a':
            #     print("The first is {0} the second is {1}".format(len1, len2))
        return maxArr
