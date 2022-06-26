
"""
在 D 天内送达包裹的能力（Medium）
https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/
"""
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 二分答案 判定问题
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if self.valid(weights, mid, days):
                right = mid
            else:
                left = mid + 1

        return right

    def valid(self, weights, n, days) -> bool:
        cnt = 1
        sum_ = 0
        for i in weights:
            if sum_ + i <= n:
                sum_ += i
            else:
                cnt += 1
                if cnt > days:
                    return False
                sum_ = i

        return True
