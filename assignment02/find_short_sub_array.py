class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ans = {}  # num:[count, first_index,end_index]
        for index, num in enumerate(nums):
            if num in ans:
                # 次数+1
                ans[num][0] += 1
                # 更改end_index
                ans[num][-1] = index
            else:
                ans[num] = [1, index, index]
        # 最短子数组 end - first
        degree = 0
        length = 50001
        for count, first_index, end_index in ans.values():
            _len = end_index - first_index + 1
            if count > degree:
                degree = count
                length = _len
            # 需要注意相等的情况
            elif count == degree:
                if _len < length:
                    length = _len
        return length
