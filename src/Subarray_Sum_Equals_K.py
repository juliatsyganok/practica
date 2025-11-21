from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                pre[i] = nums[i]
            else:
                pre[i] = pre[i - 1] + nums[i]
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == 0:
                    sam = pre[j]
                else:
                    sam = pre[j] - pre[i - 1]
                
                if sam == k:
                    cnt += 1
        
        return cnt
        

        