
"""
滑动窗口最大值（Hard）
https://leetcode-cn.com/problems/sliding-window-maximum/
"""
from typing import List


class Solution:
    # todo 比较慢
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deque = []
        for i in range(len(nums)):
            # 滑窗超过队首元素时，队首元素出队
            while len(deque) > 0 and nums[i] > nums[deque[len(deque) - 1]]:
                deque.pop()
            deque.append(i)
            if i - deque[0] >= k:
                deque.pop(0)
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res
