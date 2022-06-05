from typing import List


# plus-one
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """

        思路：
        +1 从末位开始算，逢10进1
        认为digits是一个栈， 从栈顶(末位)pop一位，+1 ，
            如果进位，递归调用+1 补0，否则直接+1 进栈
        边界条件 栈可能传入[](pop之后进入函数) 这时直接补1

        :param digits:
        :return:
        """
        if not digits:
            digits.append(1)
            return digits
        if digits[0] == 0:
            digits[0] = 1
            return digits
        else:
            c = digits.pop(-1)
            if c == 9:
                digits = self.plusOne(digits)
                digits.append(0)
                return digits
            else:
                digits.append(c+1)
                return digits


# 还有遍历找9的解法
