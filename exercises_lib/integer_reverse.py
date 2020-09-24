# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#  示例 1:
#  输入: 123
# 输出: 321
#  示例 2:
#  输入: -123
# 输出: -321
#  示例 3:
#  输入: 120
# 输出: 21
#  假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        if x >= 0:
            ln = len(str(x))
            for i in range(ln):
                array = ln - i - 1
                res = x // pow(10, array)
                x -= res * pow(10, array)
                ans += res * pow(10, i)
                if ans > pow(2, 31) - 1:
                    return 0
        else:
            ln = len(str(x)) - 1
            for i in range(ln):
                array = ln - i - 1
                res = abs(x) // pow(10, array)
                x -= -res * pow(10, array)
                ans += -res * pow(10, i)
                if ans < pow(-2, 31):
                    return 0
        return ans

