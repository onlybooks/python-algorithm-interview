from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(i: int) -> int:
            if i < 0:
                return 0
            return max(_rob(i - 1), _rob(i - 2) + nums[i])

        return _rob(len(nums) - 1)
