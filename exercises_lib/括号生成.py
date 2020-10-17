# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#  示例：
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        _ans = ''

        def parenthesis(_ans, left, right):
            if left < right:
                return
            if left < n:
                parenthesis(_ans+'(', left+1, right)
            if right < left:
                parenthesis(_ans+')', left, right+1)
            if right == n:
                ans.append(_ans)
        parenthesis(_ans, 0, 0)
        return ans


if __name__ == '__main__':
    n = 1
    test = Solution()
    res = test.generateParenthesis(n)
    print(res)

