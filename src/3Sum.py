from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            le, ri = i + 1, n - 1
            while le < ri:
                summ = nums[i] + nums[le] + nums[ri]
                if summ == 0:
                    res.append([nums[i], nums[le], nums[ri]])
                    while le < ri and nums[le] == nums[le + 1]:
                        le += 1
                    while le < ri and nums[ri] == nums[ri - 1]:
                        ri -= 1
                    le += 1
                    ri -= 1
                elif summ < 0:
                    le += 1
                else:
                    ri -= 1  
        return res