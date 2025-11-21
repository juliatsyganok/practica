from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        s_l = 0
        for i in s:
            if i - 1 not in s:
                tek = i
                tek_le = 1
                while tek + 1 in s:
                    tek += 1
                    tek_le += 1
                s_l = max(s_l, tek_le)