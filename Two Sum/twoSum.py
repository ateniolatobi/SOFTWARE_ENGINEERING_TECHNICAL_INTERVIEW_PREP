from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        count_dict = Counter(nums)
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        second = 0
        first = 0
        found = False
        i1 = 0
        i2 = 0
        for k, v in num_dict.items():
            if (target-k) in num_dict:
                if k == (target - k):
                    if count_dict[k] > 1:                 
                        i2 = num_dict[k]
                        i1 = nums.index(k)
                        break
                    else:
                        continue
                i1 = num_dict[k]
                i2 = num_dict[target-k]
                break 
        return [i1, i2]
            
