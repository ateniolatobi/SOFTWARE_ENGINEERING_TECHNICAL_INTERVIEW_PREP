import statistics
class Solution:
    def merge(self, first_half, second_half):
        size = len(first_half) + len(second_half)
        arr = []
        for i in range(size):
            if not second_half or (first_half and first_half[0] <= second_half[0]):
                arr.append(first_half[0])
                first_half.pop(0)
            else:
                arr.append(second_half[0])
                second_half.pop(0)
        return arr
                
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = self.merge(nums1, nums2)
        ans = statistics.median(arr)
        return ans
