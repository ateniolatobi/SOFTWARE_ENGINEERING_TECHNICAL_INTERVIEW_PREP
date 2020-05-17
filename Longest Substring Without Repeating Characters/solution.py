class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "pwwkew"
        start, maxArr = 0, 0
        maxArr = 0
        a = {}
        for i in range(len(s)):
            if s[i] in a and a[s[i]] >= start:
                start = a[s[i]] + 1
            a[s[i]] = i
            maxArr = max(maxArr, i - start + 1)
        return maxArr
