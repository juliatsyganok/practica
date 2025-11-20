from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = set([x for x in range(1, n + 1)])
        nums = set(nums)
        return list(a - nums)
        
